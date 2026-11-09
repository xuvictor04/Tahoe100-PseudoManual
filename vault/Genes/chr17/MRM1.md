---
symbol: "MRM1"
type: "gene"
col: 15918
ensembl_id: "ENSG00000278619"
name: "mitochondrial rRNA methyltransferase 1"
location: "17q12"
module: 5
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MRM1

*mitochondrial rRNA methyltransferase 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +9.7, q 1e-19, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.642× (z -5.3, q 7e-05, down in 18 of 29 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.551× (z -4.8, q 4e-04, down in 16 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGW]] (+0.73, fdr 9e-06), [[CCNJ]] (+0.72, fdr 1e-05), [[DHX37]] (+0.72, fdr 7e-06); moves opposite to [[MAGT1]] (-0.64, fdr 1e-05), [[PJA2]] (-0.63, fdr 1e-05), [[GNAI2]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.7 | 1e-19 | 21/29 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +8.9 | 2e-16 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.2 | 1e-07 | 9/24 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.9 | 5e-07 | 5/13 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +5.3 | 9e-06 | 1/3 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +5.3 | 9e-06 | 18/42 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.0 | 4e-05 | 11/43 (A-172, NCI-H2347, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +5.0 | 5e-05 | 5/43 (SK-MEL-2, HS-578T, …) | rises with dose | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.77×** | +4.6 | 3e-04 | 4/22 (SK-MEL-2, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.3 | 9e-04 | 4/13 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.8 | 0.009 | 1/12 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.076 | 5/43 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.04×** | +3.1 | 0.076 | 2/23 (NCI-H460, MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.642×** | -5.3 | 7e-05 | 18/29 (BT-474, SW480, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -4.8 | 4e-04 | 16/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.576×** | -4.7 | 6e-04 | 19/43 (C-33 A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.611×** | -4.2 | 0.005 | 16/44 (J82, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -3.8 | 0.014 | 16/41 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.689× | -3.1 | 0.14 | 6/19 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.690× | -3.1 | 0.14 | 13/43 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.772× | -3.1 | 0.14 | 15/43 (SW1417, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 2.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0501× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 4.85 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0448× (z -10.0) |
| [[PANC-1 (line)]] | alt | 2.68 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0716× (z -10.6) |
| [[SW1417 (line)]] | alt | 2.48 | 0 | 1 (1 ⚠) | — | [[Ribociclib (drug)]] 0.5 µM 0.0498× (z -8.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.664 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGW]] | +0.73 | +0.66 / +0.57 | both halves | 9e-06 | STRING 657 |
| [[CCNJ]] | +0.72 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DHX37]] | +0.72 | +0.59 / +0.69 | both halves | 7e-06 | pathway: rRNA processing |
| [[DHX33]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TYSND1]] | +0.70 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CCDC86]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.70 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[MRTO4]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[C1orf109]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ALG8]] | +0.68 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[NOP16]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGT1]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PJA2]] | -0.63 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[GNAI2]] | -0.62 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[CAST]] | -0.62 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ALAD]] | -0.60 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[HDAC5]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.59 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ARL3]] | -0.59 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[LGALS1]] | -0.59 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[SARAF]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.57 | -0.47 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRM1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LRP1]] | C | LRP1 activity lowers MRM1's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.42× higher at baseline in the lines without LRP1 | 0.080 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.1, 10.1); signed map (24.8, -29.5). **Vector** length 51.6, 7.02% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.58 to 13); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.6 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial rRNA methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,601,583-36,608,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22578 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IN84](https://www.uniprot.org/uniprotkb/Q6IN84) (rRNA methyltransferase 1, mitochondrial):

> S-adenosyl-L-methionine-dependent 2'-O-ribose methyltransferase that catalyzes the formation of 2'-O-methylguanosine at position 1145 (Gm1145) in the 16S mitochondrial large subunit ribosomal RNA (mtLSU rRNA), a universally conserved modification in the peptidyl transferase domain of the mtLSU rRNA.

**Summary**, from NCBI Gene [79922](https://www.ncbi.nlm.nih.gov/gene/79922):

> Enables rRNA (guanosine-2'-O-ribose)-methyltransferase activity. Involved in rRNA processing. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26202) · Entrez [79922](https://www.ncbi.nlm.nih.gov/gene/79922) · UniProt [Q6IN84](https://www.uniprot.org/uniprotkb/Q6IN84) · Ensembl [ENSG00000278619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278619)

## Data

Gene col 15918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15918); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15918]; `tensor/DDL_lfc|DDL_z.npy` [15918]; `embed/gene_vectors.npy` [15918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15918 or target_col == 15918). Every well: [[MRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
