---
symbol: "TRIM3"
type: "gene"
col: 3120
ensembl_id: "ENSG00000110171"
name: "tripartite motif containing 3"
location: "11p15.4"
module: 56
arm: "+"
pooled_cpm: 16.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TRIM3

*tripartite motif containing 3* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.18× (z +9.5, q 1e-18, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.507× (z -7.8, q 5e-12, down in 21 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.665× (z -4.9, q 2e-04, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1L]] (+0.67, fdr 1e-05), [[SLC35A2]] (+0.67, fdr 7e-06), [[ASIC4]] (+0.66, fdr 7e-06); moves opposite to [[THOC7]] (-0.58, fdr 9e-05), [[MBTPS2]] (-0.56, fdr 2e-05), [[RIF1]] (-0.55, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +9.5 | 1e-18 | 40/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +8.8 | 3e-16 | 36/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +7.6 | 5e-12 | 23/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +7.3 | 4e-11 | 36/47 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.8 | 2e-04 | 20/47 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 3e-04 | 19/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +4.1 | 0.004 | 18/46 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 22/47 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.006 | 17/45 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.39×** | +3.9 | 0.006 | 14/41 (A498, NCI-H460, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.077 | 12/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.080 | 11/47 (A549, hTERT-HPNE, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.086 | 7/48 (HS-578T, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -7.8 | 5e-12 | 21/30 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.576×** | -6.8 | 3e-09 | 26/39 (LOX-IMVI, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.665×** | -4.9 | 2e-04 | 24/46 (J82, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -4.8 | 2e-04 | 25/48 (HS-578T, PANC-1, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.732×** | -3.9 | 0.012 | 19/48 (SW 1271, SW 1088, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.743×** | -3.7 | 0.020 | 16/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.751×** | -3.6 | 0.029 | 18/48 (SW 1271, SW1417, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.032 | 14/44 (A498, J82, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.049 | 14/48 (Hs 766T, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.771×** | -3.3 | 0.065 | 12/48 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.088 | 14/47 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.1 | 0.089 | 15/48 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 5 µM |  | **0.781×** | -3.1 | 0.089 | 8/47 (HS-578T, SW48, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.782×** | -3.1 | 0.089 | 11/48 (SW 1088, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0904× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 11.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +9.8) | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 2 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0517× (z -11.6) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +10.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 1 | — | [[Bexarotene (drug)]] 0.5 µM 0.0750× (z -8.5) |
| [[C32 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0811× (z -9.9) |
| [[J82 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.1) | — |
| [[LoVo (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 7.94 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.112× (z -9.7) |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0626× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +8.8) | — |
| [[A-172 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1L]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SLC35A2]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ASIC4]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TINCR]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[HPX]] | +0.65 | +0.59 / +0.71 | both halves | 7e-06 | ⚠ same locus (6.0 kb, same strand: neighbours can correlate without regulation) |
| [[TXNDC11]] | +0.65 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SRA1]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MGAT1]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HYPK]] | +0.64 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[VWCE]] | +0.63 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FAM177A1]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TFAP2E]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | -0.58 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[MBTPS2]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RIF1]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TCF12]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[AASDHPPT]] | -0.54 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[CSTF2T]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -19.9); signed map (-48.1, 16.1). **Vector** length 86.2, 17.8% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.53 to 5); *Synthesis of substrates in N-glycan biosythesis* (reactome, mean cos +0.50 to 6); *Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +3.1 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.5 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | -0.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,448,613-6,474,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HAC1, BERP, RNF97; previously RNF22 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O75382](https://www.uniprot.org/uniprotkb/O75382) (Tripartite motif-containing protein 3):

> E3 ubiquitin ligase that plays essential roles in neuronal functions such as regulation of neuronal plasticity, learning, and memory (By similarity). In addition to its neuronal functions, participates in other biological processes such as innate immunity or cell cycle regulation. Component of the cytoskeleton-associated recycling or transport complex in neurons, polyubiquitinates gamma-actin, thus regulating neuronal plasticity, learning, and memory (By similarity). Ubiquitinates postsynaptic …

**Summary**, from NCBI Gene [10612](https://www.ncbi.nlm.nih.gov/gene/10612):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family, also called the 'RING-B-box-coiled-coil' (RBCC) subgroup of RING finger proteins. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein localizes to cytoplasmic filaments. It is similar to a rat protein which is a specific partner for the tail domain of myosin V, a class of myosins which are involved in the targeted transport of …

**Accessions** — [HGNC:10064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10064) · Entrez [10612](https://www.ncbi.nlm.nih.gov/gene/10612) · UniProt [O75382](https://www.uniprot.org/uniprotkb/O75382) · Ensembl [ENSG00000110171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110171)

## Data

Gene col 3120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3120); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3120]; `tensor/DDL_lfc|DDL_z.npy` [3120]; `embed/gene_vectors.npy` [3120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3120 or target_col == 3120). Every well: [[TRIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
