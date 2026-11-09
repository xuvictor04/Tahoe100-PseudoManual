---
symbol: "IL17RC"
type: "gene"
col: 8759
ensembl_id: "ENSG00000163702"
name: "interleukin 17 receptor C"
location: "3p25.3"
module: 40
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IL17RC

*interleukin 17 receptor C* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.41× (z +4.8, q 1e-03, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.436× (z -9.8, q 4e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR107]] (+0.63, fdr 1e-05), [[NPRL2]] (+0.62, fdr 7e-06), [[CYB561D2]] (+0.62, fdr 1e-05); moves opposite to [[EIF4G3]] (-0.60, fdr 7e-06), [[PKP4]] (-0.55, fdr 2e-05), [[FJX1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 1e-03 | 16/46 (hTERT-HPNE, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +4.1 | 0.012 | 11/44 (NCI-H2030, HS-578T, …) | two highest doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.025 | 10/42 (COLO 205, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.026 | 12/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +3.6 | 0.042 | 7/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Lopinavir (drug)]] 5 µM |  | 1.25× | +3.1 | 0.17 | 7/47 (LoVo, A498, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.17 | 8/42 (HepG2/C3A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.436×** | -9.8 | 4e-20 | 35/47 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.644×** | -8.6 | 2e-15 | 27/47 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -7.7 | 3e-12 | 31/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -7.5 | 8e-12 | 27/43 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.632×** | -6.4 | 2e-08 | 20/42 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.670×** | -5.6 | 2e-06 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.645×** | -5.2 | 1e-05 | 18/39 (HS-578T, COLO 205, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.489×** | -5.2 | 1e-05 | 22/43 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.694×** | -5.1 | 2e-05 | 18/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.676×** | -4.6 | 2e-04 | 16/46 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.721×** | -4.6 | 3e-04 | 18/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.725×** | -4.5 | 3e-04 | 19/47 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.541×** | -4.5 | 3e-04 | 15/44 (PANC-1, RKO, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.731×** | -4.4 | 5e-04 | 17/47 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -4.4 | 5e-04 | 20/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.550×** | -4.3 | 5e-04 | 14/43 (RPMI-7951, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.584×** | -3.9 | 0.003 | 14/46 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.018 | 14/47 (Hs 766T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.805×** | -3.0 | 0.059 | 7/48 (A-172, H4, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -2.8 | 0.099 | 13/45 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 22.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.177× (z -8.7) |
| [[SNU-423 (line)]] | alt | 9.34 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 9.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[KATO III (line)]] | alt | 5.48 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0626× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0590× (z -9.7) |
| [[SW480 (line)]] | alt | 6.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR107]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NPRL2]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MAX]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.61 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[RINT1]] | +0.60 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[GGCX]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.59 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[MICA]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.58 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CRY2]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G3]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[PKP4]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FJX1]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[IMMP2L]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[RFX3]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[DDX10]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[AMIGO2]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TCF12]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ADGRA3]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TFAM]] | -0.52 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[LINC02516]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FOXP1]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IL17RC's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.7, -30.7); signed map (-40.7, 12.5). **Vector** length 69.8, 11.7% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -9.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 17 receptor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,917,074-9,933,630 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL17-RL |
| Gene groups (HGNC) | Interleukin receptors |
| Reactome | 8 pathways, smallest: Interleukin-17 signaling; SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAC3](https://www.uniprot.org/uniprotkb/Q8NAC3) (Interleukin-17 receptor C):

> Receptor for IL17A and IL17F, major effector cytokines of innate and adaptive immune system involved in antimicrobial host defense and maintenance of tissue integrity (By similarity). Receptor for IL17A and IL17F, major effector cytokines of innate and adaptive immune system involved in antimicrobial host defense and maintenance of tissue integrity. Receptor for IL17A and IL17F homodimers as part of a heterodimeric complex with IL17RA. Receptor for the heterodimer formed by IL17A and IL17B as …

**Summary**, from NCBI Gene [84818](https://www.ncbi.nlm.nih.gov/gene/84818):

> This gene encodes a single-pass type I membrane protein that shares similarity with the interleukin-17 receptor (IL-17RA). Unlike IL-17RA, which is predominantly expressed in hemopoietic cells, and binds with high affinity to only IL-17A, this protein is expressed in nonhemopoietic tissues, and binds both IL-17A and IL-17F with similar affinities. The proinflammatory cytokines, IL-17A and IL-17F, have been implicated in the progression of inflammatory and autoimmune diseases. Multiple …

**Accessions** — [HGNC:18358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18358) · Entrez [84818](https://www.ncbi.nlm.nih.gov/gene/84818) · UniProt [Q8NAC3](https://www.uniprot.org/uniprotkb/Q8NAC3) · Ensembl [ENSG00000163702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163702)

## Data

Gene col 8759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8759); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8759]; `tensor/DDL_lfc|DDL_z.npy` [8759]; `embed/gene_vectors.npy` [8759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8759 or target_col == 8759). Every well: [[IL17RC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL17RC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
