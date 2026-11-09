---
symbol: "LAMTOR1"
type: "gene"
col: 7369
ensembl_id: "ENSG00000149357"
name: "late endosomal/lysosomal adaptor, MAPK and MTOR activator 1"
location: "11q13.4"
module: 7
arm: "+"
pooled_cpm: 24.62
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# LAMTOR1

*late endosomal/lysosomal adaptor, MAPK and MTOR activator 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +13.0, q 1e-35, up in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.54× (z +6.4, q 2e-08, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.697× (z -5.3, q 7e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUL1]] (+0.68, fdr 7e-06), [[UNC50]] (+0.63, fdr 1e-05), [[TMEM222]] (+0.63, fdr 8e-06); moves opposite to [[PTMA]] (-0.53, fdr 1e-05), [[CBX3]] (-0.52, fdr 1e-04), [[PTMAP2]] (-0.51, fdr 1e-04, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[ARL3]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +13.0 | 1e-35 | 34/42 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +9.2 | 1e-17 | 31/36 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.4 | 2e-11 | 13/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.6 | 5e-09 | 32/39 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.4 | 2e-08 | 28/47 (A-427, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.4 | 6e-06 | 24/48 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 6e-04 | 22/44 (NCI-H460, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.006 | 18/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.007 | 21/48 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.6 | 0.021 | 19/45 (KATO III, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.029 | 18/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.3 | 0.040 | 19/43 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.057 | 16/48 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -5.3 | 7e-05 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -5.1 | 9e-05 | 24/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -4.8 | 3e-04 | 26/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -4.2 | 0.004 | 23/46 (SW480, NCI-H23, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.589×** | -4.1 | 0.006 | 15/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -3.9 | 0.007 | 21/47 (hTERT-HPNE, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.011 | 16/48 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.057 | 15/47 (SW480, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 2 (2 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.100× (z -8.9) ⚠ toxic; unreliable plate only |
| [[HEC-1-A (line)]] | alt | 19.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 18.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +9.0) | — |
| [[A-172 (line)]] | wt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.108× (z -10.1) |
| [[Hs 766T (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -8.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 30.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.442× (z -8.8) |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUL1]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[UNC50]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TMEM222]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ZDHHC4]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MANBAL]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.57 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF594]] | +0.56 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[SRSF6]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[POLDIP2]] | +0.56 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[VPS33A]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[BECN1]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 | pathway: Autophagy |
| [[DRG2]] | +0.56 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CBX3]] | -0.52 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[PTMAP2]] ⚠ | -0.51 | -0.51 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARL3]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.49 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[PLEKHH3]] | -0.49 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[ARHGEF26]] | -0.49 | -0.37 / -0.43 | both halves | 8e-05 | pathway: CDC42 GTPase cycle |
| [[CARHSP1]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RNF24]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RPS6KA5]] | -0.48 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[HDAC3]] | -0.47 | -0.52 / -0.37 | both halves | 8e-05 | pathway: Intracellular signaling by second messengers |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-41.1, 11.1); signed map (7.0, -34.4). **Vector** length 81.3, 18.1% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.9 | +7.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.5 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.4 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | late endosomal/lysosomal adaptor, MAPK and MTOR activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,085,895-72,103,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20625, p18, p27RF-Rho, Pdro, Ragulator1; previously C11orf59 |
| Gene groups (HGNC) | Ragulator complex |
| Reactome | 28 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; RHOH GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IAA8](https://www.uniprot.org/uniprotkb/Q6IAA8) (Ragulator complex protein LAMTOR1):

> Key component of the Ragulator complex, a multiprotein complex involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Activated by amino acids through a mechanism involving the lysosomal V-ATPase, the Ragulator plays a dual role for the small GTPases Rag (RagA/RRAGA, RagB/RRAGB, RagC/RRAGC and/or RagD/RRAGD): it (1) acts as a guanine nucleotide exchange factor (GEF), activating the small …

**Summary**, from NCBI Gene [55004](https://www.ncbi.nlm.nih.gov/gene/55004):

> Enables GTPase binding activity and protein-membrane adaptor activity. Contributes to guanyl-nucleotide exchange factor activity and molecular adaptor activity. Involved in several processes, including cholesterol homeostasis; positive regulation of TORC1 signaling; and regulation of cholesterol transport. Located in lysosome and plasma membrane. Part of FNIP-folliculin RagC/D GAP. Is active in Ragulator complex and lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26068) · Entrez [55004](https://www.ncbi.nlm.nih.gov/gene/55004) · UniProt [Q6IAA8](https://www.uniprot.org/uniprotkb/Q6IAA8) · Ensembl [ENSG00000149357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149357)

## Data

Gene col 7369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7369); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7369]; `tensor/DDL_lfc|DDL_z.npy` [7369]; `embed/gene_vectors.npy` [7369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7369 or target_col == 7369). Every well: [[LAMTOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
