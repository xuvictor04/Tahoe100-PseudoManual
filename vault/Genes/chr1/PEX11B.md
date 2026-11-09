---
symbol: "PEX11B"
type: "gene"
col: 5245
ensembl_id: "ENSG00000131779"
name: "peroxisomal biogenesis factor 11 beta"
location: "1q21.1"
module: 119
arm: "+"
pooled_cpm: 9.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# PEX11B

*peroxisomal biogenesis factor 11 beta* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +7.9, q 2e-12, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.718× (z -7.7, q 6e-12, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTI2]] (+0.67, fdr 1e-05), [[ALKBH4]] (+0.64, fdr 1e-05), [[KANSL2]] (+0.62, fdr 1e-05); moves opposite to [[TBILA]] (-0.55, fdr 3e-05), [[MAPRE1]] (-0.54, fdr 4e-05), [[TXNRD1]] (-0.54, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.9 | 2e-12 | 21/44 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.4 | 3e-11 | 19/39 (SW1417, SW 900, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.7 | 4e-09 | 23/48 (KATO III, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.0 | 8e-05 | 13/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.001 | 18/46 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 3/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.0 | 0.005 | 8/20 (A549, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.007 | 11/43 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.018 | 8/45 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.044 | 7/45 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.061 | 4/41 (NCI-H23, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.061 | 7/47 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +3.0 | 0.12 | 9/45 (A-427, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.718×** | -7.7 | 6e-12 | 27/47 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.662×** | -6.8 | 3e-09 | 20/34 (HT-29, C32, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -5.1 | 7e-05 | 17/46 (COLO 205, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -5.0 | 7e-05 | 14/21 (J82, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.740×** | -5.0 | 8e-05 | 16/45 (hTERT-HPNE, SNU-423, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.750×** | -4.7 | 2e-04 | 15/45 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.778×** | -4.0 | 0.006 | 12/41 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.007 | 17/44 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.007 | 12/45 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.040 | 10/47 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.050 | 12/45 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.058 | 9/45 (SNU-1, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -3.2 | 0.058 | 4/47 (SW 1271, SNU-423, …) | all doses, flat |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.060 | 6/45 (HCT15, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.832×** | -3.0 | 0.094 | 7/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 10.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0695× (z -13.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.9) |
| [[SNU-423 (line)]] | alt | 7.57 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.132× (z -9.5) |
| [[H4 (line)]] | wt | 7.93 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0592× (z -8.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0807× (z -11.4) |
| [[HT-29 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTI2]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.64 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[KANSL2]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[NDUFS3]] | +0.62 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[TARS2]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ZNF500]] | +0.60 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[TMEM216]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RPUSD2]] | +0.58 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ZNF251]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ACADS]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.57 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[VPS33B]] | +0.57 | +0.40 / +0.64 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBILA]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TXNRD1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[GLS]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CREB5]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RBBP8]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DYNC1H1]] | -0.50 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[SEL1L3]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TUSC3]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 | pathway: Protein localization |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-51.7, 4.6); signed map (-10.0, -12.2). **Vector** length 63.8, 9.46% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +2.5 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 11 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,911,350-145,918,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEX11beta, PEX11β |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | PEROXISOME |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O96011](https://www.uniprot.org/uniprotkb/O96011) (Peroxisomal membrane protein 11B):

> Involved in peroxisomal proliferation. May regulate peroxisome division by recruiting the dynamin-related GTPase DNM1L to the peroxisomal membrane. Promotes membrane protrusion and elongation on the peroxisomal surface.

**Summary**, from NCBI Gene [8799](https://www.ncbi.nlm.nih.gov/gene/8799):

> The protein encoded by this gene facilitates peroxisomal proliferation and interacts with PEX19. The encoded protein is found in the peroxisomal membrane. Several transcript variants, some protein-coding and some not protein-coding, have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:8853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8853) · Entrez [8799](https://www.ncbi.nlm.nih.gov/gene/8799) · UniProt [O96011](https://www.uniprot.org/uniprotkb/O96011) · Ensembl [ENSG00000131779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131779)

## Data

Gene col 5245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5245); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5245]; `tensor/DDL_lfc|DDL_z.npy` [5245]; `embed/gene_vectors.npy` [5245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5245 or target_col == 5245). Every well: [[PEX11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
