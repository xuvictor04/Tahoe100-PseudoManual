---
symbol: "PPAN"
type: "gene"
col: 5130
ensembl_id: "ENSG00000130810"
name: "peter pan homolog"
location: "19p13.2"
module: 5
arm: "+"
pooled_cpm: 18.6
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PPAN

*peter pan homolog* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 12.9× (z +19.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.667× (z -6.0, q 1e-06, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSR1]] (+0.80, fdr 7e-06), [[MRTO4]] (+0.75, fdr 7e-06), [[BYSL]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **12.9×** | +19.9 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **7.11×** | +15.2 | 0e+00 | 39/44 (HEC-1-A, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +9.0 | 3e-17 | 34/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.9 | 8e-10 | 26/36 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 23/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.88×** | +4.9 | 9e-05 | 18/45 (A498, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.8 | 1e-04 | 19/42 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 5e-04 | 17/47 (LS 180, RKO, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +4.4 | 8e-04 | 14/46 (Hs 766T, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.74×** | +4.3 | 1e-03 | 12/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.002 | 10/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 20/48 (NCI-H2347, HOP62, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 17/47 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.006 | 16/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.006 | 16/47 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.006 | 11/47 (BT-474, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.017 | 15/47 (C32, SNU-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.029 | 10/46 (PANC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.667×** | -6.0 | 1e-06 | 27/47 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.694×** | -5.4 | 2e-05 | 20/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -5.2 | 5e-05 | 21/48 (A498, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.003 | 20/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.588×** | -4.1 | 0.004 | 16/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.762×** | -4.0 | 0.006 | 12/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.0 | 0.006 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.033 | 16/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.4 | 0.037 | 18/47 (C32, RKO, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.075 | 12/48 (A498, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.9 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 13.4× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 23.1 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.31× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.331× (z -9.0) |
| [[C32 (line)]] | wt | 33.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -10.9) |
| [[HS-578T (line)]] | alt | 17.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 24.1× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 25.0 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 24.4× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 14.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 22.2× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.9× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 19.1 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.346× (z -9.1) |
| [[SW480 (line)]] | alt | 15.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 18.1× (z +9.8) | — |
| [[A-427 (line)]] | wt | 24.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.0× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0927× (z -8.9) |
| [[LoVo (line)]] | wt | 17.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.0× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.8× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR1]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; STRING 614 |
| [[MRTO4]] | +0.75 | +0.77 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 919 |
| [[BYSL]] | +0.75 | +0.77 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 819 |
| [[NAT10]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 | STRING 651 |
| [[TBRG4]] | +0.71 | +0.72 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V2 |
| [[TWNK]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | STRING 849 |
| [[GRWD1]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 812 |
| [[PES1]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 955 |
| [[NOP2]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 781 |
| [[POLR1A]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 | STRING 575 |
| [[NOM1]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers PPAN's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.59× higher at baseline in the lines without RALGPS2 | 0.070 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PPAN's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PPAN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.9, -36.9); signed map (-2.0, -46.5). **Vector** length 104, 24.2% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.3 | +19.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.6 | +15.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +9.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | peter pan homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,106,362-10,112,012 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSF1, SSF2, SSF, BXDC3 |
| Gene groups (HGNC) | Brix domain containing; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ55](https://www.uniprot.org/uniprotkb/Q9NQ55) (Suppressor of SWI4 1 homolog):

> May have a role in cell growth.

**Summary**, from NCBI Gene [56342](https://www.ncbi.nlm.nih.gov/gene/56342):

> The protein encoded by this gene is an evolutionarily conserved protein similar to yeast SSF1 as well as to the gene product of the Drosophila gene peter pan (ppan). SSF1 is known to be involved in the second step of mRNA splicing. Both SSF1 and ppan are essential for cell growth and proliferation. Exogenous expression of this gene was reported to reduce the anchorage-independent growth of some tumor cells. Read-through transcription of this gene with P2RY11/P2Y(11), an adjacent downstream gene …

**Accessions** — [HGNC:9227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9227) · Entrez [56342](https://www.ncbi.nlm.nih.gov/gene/56342) · UniProt [Q9NQ55](https://www.uniprot.org/uniprotkb/Q9NQ55) · Ensembl [ENSG00000130810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130810)

## Data

Gene col 5130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5130); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5130]; `tensor/DDL_lfc|DDL_z.npy` [5130]; `embed/gene_vectors.npy` [5130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5130 or target_col == 5130). Every well: [[PPAN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPAN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
