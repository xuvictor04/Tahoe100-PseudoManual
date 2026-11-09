---
symbol: "DPP3"
type: "gene"
col: 14905
ensembl_id: "ENSG00000254986"
name: "dipeptidyl peptidase 3"
location: "11q13.2"
module: 4
arm: "+"
pooled_cpm: 12.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DPP3

*dipeptidyl peptidase 3* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.62× (z +15.0, q 0e+00, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.78× (z +9.0, q 4e-17, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.682× (z -8.4, q 2e-14, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT7]] (+0.68, fdr 7e-06), [[PSMC3]] (+0.66, fdr 7e-06), [[PSME3]] (+0.65, fdr 7e-06); moves opposite to [[GPX4]] (-0.65, fdr 1e-05), [[MINDY2]] (-0.61, fdr 1e-05), [[AFTPH]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +15.0 | 0e+00 | 37/38 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +12.0 | 7e-31 | 18/20 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +9.1 | 1e-17 | 22/30 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +9.0 | 4e-17 | 34/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +8.6 | 1e-15 | 28/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +7.8 | 6e-13 | 33/45 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.55×** | +6.5 | 5e-09 | 20/42 (A-427, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +5.6 | 1e-06 | 24/47 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.32×** | +4.3 | 9e-04 | 9/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.002 | 8/42 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.8 | 0.006 | 7/28 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.8 | 0.006 | 7/34 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +3.8 | 0.006 | 12/48 (Panc 03.27, A-427, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.013 | 15/46 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.18× | +3.6 | 0.013 | 16/46 (A549, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.017 | 8/48 (SW480, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.018 | 13/46 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.023 | 11/44 (SW1417, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.074 | 6/41 (SW480, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -8.4 | 2e-14 | 29/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -6.9 | 1e-09 | 25/47 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -5.8 | 1e-06 | 22/47 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.595×** | -4.2 | 0.003 | 19/47 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.772×** | -4.0 | 0.006 | 18/46 (BT-474, SW1417, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.010 | 17/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.012 | 12/47 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.787×** | -3.7 | 0.012 | 12/47 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.012 | 13/45 (C-33 A, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -3.7 | 0.012 | 16/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.013 | 18/47 (SW1417, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.792×** | -3.6 | 0.013 | 15/45 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -3.6 | 0.013 | 15/48 (MIA PaCa-2, KATO III, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.015 | 14/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.797×** | -3.5 | 0.015 | 12/46 (hTERT-HPNE, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.017 | 15/47 (KATO III, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.017 | 8/47 (SW 1271, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0894× (z -13.0) |
| [[C32 (line)]] | wt | 8.74 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.113× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 7.40 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0849× (z -9.1) |
| [[J82 (line)]] | alt | 13.4 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.227× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -8.7) |
| [[PANC-1 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT7]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PSMC3]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[PSME3]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DHX37]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PSMC5]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 | pathway: Cellular response to chemical stress |
| [[NIT2]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[EXOC7]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[DMAC2]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[WDR77]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[MRPS7]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[RCC1L]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SARS2]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX4]] | -0.65 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[UGCG]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.57 | -0.56 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PURA]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[MARCHF9]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[YTHDC1]] | -0.56 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SERF2]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.8, -30.0); signed map (-7.2, -36.6). **Vector** length 79.1, 14.1% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.3 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,480,013-66,509,657 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M49 metallopeptidase family |
| Reactome | 5 pathways, smallest: KEAP1-NFE2L2 pathway; Cellular response to chemical stress; Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY33](https://www.uniprot.org/uniprotkb/Q9NY33) (Dipeptidyl peptidase 3):

> Cleaves and degrades bioactive peptides, including angiotensin, Leu-enkephalin and Met-enkephalin. Also cleaves Arg-Arg-beta-naphthylamide (in vitro).

**Summary**, from NCBI Gene [10072](https://www.ncbi.nlm.nih.gov/gene/10072):

> This gene encodes a protein that is a member of the M49 family of metallopeptidases. This cytoplasmic protein binds a single zinc ion with its zinc-binding motif (HELLGH) and has post-proline dipeptidyl aminopeptidase activity, cleaving Xaa-Pro dipeptides from the N-termini of proteins. Increased activity of this protein is associated with endometrial and ovarian cancers. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:3008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3008) · Entrez [10072](https://www.ncbi.nlm.nih.gov/gene/10072) · UniProt [Q9NY33](https://www.uniprot.org/uniprotkb/Q9NY33) · Ensembl [ENSG00000254986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254986)

## Data

Gene col 14905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14905); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14905]; `tensor/DDL_lfc|DDL_z.npy` [14905]; `embed/gene_vectors.npy` [14905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14905 or target_col == 14905). Every well: [[DPP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
