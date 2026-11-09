---
symbol: "RORA-AS1"
type: "gene"
col: 14431
ensembl_id: "ENSG00000245534"
name: "RORA antisense RNA 1"
location: "15q22.2"
module: 26
arm: "+"
pooled_cpm: 20.72
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RORA-AS1

*RORA antisense RNA 1* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +13.0, q 4e-36, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.813× (z -5.3, q 6e-05, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.63, fdr 1e-05), [[LINC02762]] (+0.63, fdr 1e-05), [[DARS1-AS1]] (+0.61, fdr 1e-05); moves opposite to [[MTMR9]] (-0.51, fdr 6e-05), [[MON1A]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +13.0 | 4e-36 | 39/47 (Hs 766T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +11.2 | 1e-26 | 35/47 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.7 | 4e-16 | 33/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +8.2 | 4e-14 | 28/48 (AsPC-1, SW480, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.9 | 2e-13 | 26/48 (A549, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.7 | 1e-12 | 34/48 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.6 | 3e-12 | 22/35 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.4 | 9e-12 | 21/41 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.9 | 2e-10 | 26/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +5.4 | 4e-06 | 18/47 (A549, AsPC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.9 | 5e-05 | 16/44 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.8 | 6e-05 | 18/47 (LoVo, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.8 | 8e-05 | 18/47 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 14/47 (SW1417, J82, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 14/47 (A549, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.031 | 8/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.046 | 11/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.086 | 9/47 (NCI-H460, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.086 | 8/47 (KATO III, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -5.3 | 6e-05 | 17/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -5.1 | 1e-04 | 20/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.801×** | -3.9 | 0.014 | 15/47 (H4, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.809×** | -3.8 | 0.014 | 17/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.811×** | -3.8 | 0.014 | 12/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.811×** | -3.8 | 0.014 | 16/48 (KATO III, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.823×** | -3.5 | 0.036 | 11/47 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.043 | 8/47 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.4 | 0.043 | 10/46 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.4 | 0.043 | 4/48 (hTERT-HPNE, C32, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.051 | 7/47 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.137× (z -9.9) |
| [[H4 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Monocrotaline (drug)]] 0.05 µM 0.0737× (z -10.9) |
| [[KATO III (line)]] | alt | 52.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.94× (z +9.0) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 1 | — | [[Pemigatinib (drug)]] 5 µM 0.0404× (z -8.8) |
| [[SW48 (line)]] | wt | 31.1 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.117× (z -9.7) |
| [[SW480 (line)]] | alt | 23.8 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LINC02762]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 | same gene group |
| [[ALG1L9P]] | +0.61 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 | same gene group |
| [[SGK2]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[STX17-DT]] | +0.60 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TTC41P]] | +0.60 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[DDX59-AS1]] | +0.59 | +0.60 / +0.43 | both halves | 4e-05 | same gene group |
| [[CCDC30]] | +0.59 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[LSMEM1]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[CASS4]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR9]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[MON1A]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RORA-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.8, 19.8); signed map (26.8, -1.9). **Vector** length 70.4, 11.7% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.2 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RORA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q22.2 — chr15:60,479,152-60,630,637 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51410) · Entrez [101928784](https://www.ncbi.nlm.nih.gov/gene/101928784) · Ensembl [ENSG00000245534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245534)

## Data

Gene col 14431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14431); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14431]; `tensor/DDL_lfc|DDL_z.npy` [14431]; `embed/gene_vectors.npy` [14431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14431 or target_col == 14431). Every well: [[RORA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RORA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
