---
symbol: "RIOX2"
type: "gene"
col: 10012
ensembl_id: "ENSG00000170854"
name: "ribosomal oxygenase 2"
location: "3q11.2"
module: 1
arm: "+"
pooled_cpm: 20.24
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RIOX2

*ribosomal oxygenase 2* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.10× (z +13.6, q 3e-39, up in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.61× (z +8.4, q 8e-15, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.613× (z -12.6, q 9e-34, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF17]] (+0.80, fdr 7e-06), [[TXNRD3]] (+0.78, fdr 7e-06), [[ATIC]] (+0.77, fdr 7e-06); moves opposite to [[TSC22D4]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +13.6 | 3e-39 | 32/43 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +11.4 | 2e-27 | 24/28 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +8.5 | 4e-15 | 25/37 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.61×** | +8.4 | 8e-15 | 32/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 3e-11 | 29/46 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +6.5 | 8e-09 | 24/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.9 | 3e-07 | 26/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 3e-07 | 22/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +5.0 | 3e-05 | 20/45 (NCI-H2347, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +4.9 | 5e-05 | 16/44 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 5e-05 | 17/46 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +4.8 | 9e-05 | 21/46 (Hs 766T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 13/47 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 17/45 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.3 | 7e-04 | 13/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.010 | 15/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.016 | 5/48 (LS 180, SNU-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.022 | 10/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.052 | 9/45 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.613×** | -12.6 | 9e-34 | 31/47 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -11.0 | 9e-26 | 33/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -10.9 | 2e-25 | 30/48 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -10.5 | 9e-24 | 29/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -7.4 | 1e-11 | 29/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.675×** | -7.2 | 6e-11 | 25/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -7.0 | 2e-10 | 24/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -6.3 | 2e-08 | 25/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -6.2 | 3e-08 | 24/46 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -5.2 | 1e-05 | 21/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.771×** | -4.7 | 1e-04 | 22/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.800×** | -4.1 | 0.002 | 17/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.801×** | -3.8 | 0.006 | 18/48 (SW48, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.827×** | -3.5 | 0.022 | 15/47 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.834× | -3.3 | 0.036 | 11/48 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.036 | 10/47 (A-427, RKO, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.714×** | -3.2 | 0.044 | 16/45 (RPMI-7951, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.089 | 17/48 (A498, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -19.1) |
| [[J82 (line)]] | alt | 23.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -12.7) |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0390× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -14.8) |
| [[RKO (line)]] | wt | 36.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -17.8) |
| [[SW480 (line)]] | alt | 18.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -9.5) |
| [[A498 (line)]] | wt | 21.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.1) |
| [[A-427 (line)]] | wt | 45.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.0) |
| [[LoVo (line)]] | wt | 26.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.9) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.6) |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -12.9) |
| [[SNU-423 (line)]] | alt | 9.19 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0956× (z -9.7) |
| [[SW48 (line)]] | wt | 30.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -9.3) |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF17]] | +0.80 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[TXNRD3]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ATIC]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.77 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[DPH5]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| [[ZNF485]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[POGK]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[PDCD2]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[DTD2]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[AIMP2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[LETM1]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.5, -37.9); signed map (-0.9, -40.8). **Vector** length 106, 26.1% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 23); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +8.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal oxygenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:97,941,818-97,972,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MINA53, FLJ14393, mdig, NO52, JMJD10; previously MINA |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Reactome | 5 pathways, smallest: Protein hydroxylation; HDMs demethylate histones; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUF8](https://www.uniprot.org/uniprotkb/Q8IUF8) (Ribosomal oxygenase 2):

> Oxygenase that can act as both a histone lysine demethylase and a ribosomal histidine hydroxylase. Is involved in the demethylation of trimethylated 'Lys-9' on histone H3 (H3K9me3), leading to an increase in ribosomal RNA expression. Also catalyzes the hydroxylation of 60S ribosomal protein L27a on 'His-39'. May play an important role in cell growth and survival. May be involved in ribosome biogenesis, most likely during the assembly process of pre-ribosomal particles.

**Summary**, from NCBI Gene [84864](https://www.ncbi.nlm.nih.gov/gene/84864):

> MINA is a c-Myc (MYC; MIM 190080) target gene that may play a role in cell proliferation or regulation of cell growth. (Tsuneoka et al., 2002 [PubMed 12091391]; Zhang et al., 2005 [PubMed 15897898]).[supplied by OMIM, May 2008]

**Accessions** — [HGNC:19441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19441) · Entrez [84864](https://www.ncbi.nlm.nih.gov/gene/84864) · UniProt [Q8IUF8](https://www.uniprot.org/uniprotkb/Q8IUF8) · Ensembl [ENSG00000170854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170854)

## Data

Gene col 10012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10012); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10012]; `tensor/DDL_lfc|DDL_z.npy` [10012]; `embed/gene_vectors.npy` [10012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10012 or target_col == 10012). Every well: [[RIOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
