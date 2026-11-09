---
symbol: "KAT8"
type: "gene"
col: 2377
ensembl_id: "ENSG00000103510"
name: "lysine acetyltransferase 8"
location: "16p11.2"
module: 5
arm: "+"
pooled_cpm: 19.8
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KAT8

*lysine acetyltransferase 8* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.52× (z +9.2, q 1e-17, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.633× (z -10.1, q 3e-21, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZF1]] (+0.65, fdr 7e-06), [[SYMPK]] (+0.61, fdr 1e-05), [[SSU72]] (+0.58, fdr 4e-05); moves opposite to [[HPF1]] (-0.51, fdr 4e-05), [[TEC]] (-0.48, fdr 1e-04), [[ZC2HC1A]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +9.2 | 1e-17 | 32/47 (SNU-423, HCT15, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +6.7 | 4e-09 | 25/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.5 | 2e-08 | 23/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.3 | 3e-08 | 20/46 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.3 | 3e-08 | 16/34 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.3 | 1e-05 | 17/42 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +5.0 | 4e-05 | 16/48 (A498, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.8 | 1e-04 | 19/44 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.7 | 1e-04 | 19/38 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 3e-04 | 14/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.7 | 0.012 | 11/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -10.1 | 3e-21 | 33/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.788×** | -7.4 | 2e-11 | 28/47 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -7.4 | 2e-11 | 27/48 (SW48, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.742×** | -6.6 | 6e-09 | 22/48 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.824×** | -6.0 | 2e-07 | 17/48 (SK-MEL-2, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -5.9 | 3e-07 | 19/48 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -5.6 | 1e-06 | 14/46 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -4.0 | 0.005 | 14/47 (LOX-IMVI, A-427, …) | top dose only | composition shift |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.007 | 10/47 (SK-MEL-2, LoVo, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.846× | -3.7 | 0.012 | 17/47 (NCI-H661, A-172, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.055 | 6/48 (LoVo, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.862× | -3.1 | 0.078 | 10/47 (HEC-1-A, A498, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.869× | -3.1 | 0.084 | 10/47 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.766×** | -3.1 | 0.084 | 7/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 16.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -11.8) |
| [[A-172 (line)]] | wt | 23.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.6) |
| [[A-427 (line)]] | wt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.6) |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.6) |
| [[KATO III (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.5) |
| [[SW1417 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.123× (z -8.5) |
| [[A498 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SYMPK]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SSU72]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[DIDO1]] | +0.57 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[LY6G5B]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[UBE2G2]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NDUFA10]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TMEM138]] | +0.53 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[LENG8]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CUL4A]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZNF740]] | +0.52 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SENP3]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 | STRING 910 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TEC]] | -0.48 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ZC2HC1A]] | -0.47 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TCAF1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[VEZT]] | -0.46 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ATP8B1]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TPR]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ABI1]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[RIPK2]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[RP9]] | -0.44 | -0.46 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KAT8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.3, -29.9); signed map (-8.7, -41.4). **Vector** length 72.1, 11.6% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.6 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.1 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -10.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Hexylresorcinol (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,114,489-31,131,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOF, FLJ14040, hMOF; previously MYST1 |
| Gene groups (HGNC) | MSL histone acetyltransferase complex; NSL histone acetyltransferase complex; MYST type domain containing lysine acetyltransferases; Zinc fingers MYST C2HC-type |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7Z6](https://www.uniprot.org/uniprotkb/Q9H7Z6) (Histone acetyltransferase KAT8):

> Histone acetyltransferase that catalyzes histone H4 acetylation at 'Lys-5'- and 'Lys-8' (H4K5ac and H4K8ac) or 'Lys-16' (H4K16ac), depending on the context. Catalytic component of the MSL histone acetyltransferase complex, a multiprotein complex that mediates the majority of histone H4 acetylation at 'Lys-16' (H4K16ac), an epigenetic mark that prevents chromatin compaction. H4K16ac constitutes the only acetylation mark intergenerationally transmitted and regulates key biological processes, such …

**Summary**, from NCBI Gene [84148](https://www.ncbi.nlm.nih.gov/gene/84148):

> This gene encodes a member of the MYST histone acetylase protein family. The encoded protein has a characteristic MYST domain containing an acetyl-CoA-binding site, a chromodomain typical of proteins which bind histones, and a C2HC-type zinc finger. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:17933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17933) · Entrez [84148](https://www.ncbi.nlm.nih.gov/gene/84148) · UniProt [Q9H7Z6](https://www.uniprot.org/uniprotkb/Q9H7Z6) · Ensembl [ENSG00000103510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103510)

## Data

Gene col 2377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2377); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2377]; `tensor/DDL_lfc|DDL_z.npy` [2377]; `embed/gene_vectors.npy` [2377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2377 or target_col == 2377). Every well: [[KAT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
