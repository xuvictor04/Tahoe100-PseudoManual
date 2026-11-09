---
symbol: "MCM3AP"
type: "gene"
col: 8334
ensembl_id: "ENSG00000160294"
name: "minichromosome maintenance complex component 3 associated protein"
location: "21q22.3"
module: 5
arm: "+"
pooled_cpm: 54.56
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MCM3AP

*minichromosome maintenance complex component 3 associated protein* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.32× (z +4.5, q 0.004, up in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.53× (z +3.9, q 0.022, up in 20 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 2.45×, COLO 205 2.14×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.791× (z -5.7, q 5e-06, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK5]] (+0.76, fdr 7e-06), [[DNAJC11]] (+0.75, fdr 7e-06), [[ABCF2]] (+0.72, fdr 7e-06); moves opposite to [[RNF114]] (-0.71, fdr 7e-06), [[RAB8B]] (-0.71, fdr 7e-06), [[TNNI3]] (-0.68, fdr 8e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ATP1B1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 2.45×, COLO 205 2.14×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +4.5 | 0.004 | 28/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.4 | 0.004 | 19/48 (NCI-H2030, COLO 205, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.022 | 20/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.6 | 0.033 | 19/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.6 | 0.033 | 22/43 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.072 | 14/49 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.20× | +3.1 | 0.15 | 19/48 (PANC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -5.7 | 5e-06 | 36/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -5.5 | 9e-06 | 37/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 5e-04 | 30/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.016 | 22/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.813×** | -3.6 | 0.037 | 20/48 (SW480, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.832× | -3.1 | 0.21 | 20/47 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 49.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.122× (z -9.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 78.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.498× (z -9.8) |
| [[C-33 A (line)]] | alt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.145× (z -8.7) |
| [[RKO (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -18.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 1 | — | [[Aspirin (drug)]] 5 µM 0.0714× (z -8.8) |
| [[SW 900 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.103× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | +0.76 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.75 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.72 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[ALG8]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[REXO1]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SSU72]] | +0.69 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[VPS52]] | +0.68 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PSME3]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[KMT2D]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[EMG1]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MFN2]] | +0.66 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[UTP20]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF114]] | -0.71 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[RAB8B]] | -0.71 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[TNNI3]] | -0.68 | -0.57 / -0.64 | both halves | 8e-06 |  |
| [[ANKRD37]] | -0.65 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.65 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.65 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[RYBP]] | -0.65 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.64 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[UGCG]] | -0.64 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[FHIP1A]] | -0.64 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MIEN1]] | -0.63 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[TSC22D2]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ATP1B1 activity lowers MCM3AP's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without ATP1B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[TNFRSF11A]] | B | TNFRSF11A activity lowers MCM3AP's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TNFRSF11A | 0.011 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity lowers MCM3AP's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.23× higher at baseline in the lines without IRF6 | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MCM3AP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MCM3AP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPRC5A]] | B | GPRC5A activity lowers MCM3AP's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.25× higher at baseline in the lines without GPRC5A | 0.047 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ELF3]] | B | ELF3 activity lowers MCM3AP's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.23× higher at baseline in the lines without ELF3 | 0.052 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[RHOV]] | B | RHOV activity lowers MCM3AP's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.21× higher at baseline in the lines without RHOV | 0.054 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[WFDC2]] | B | WFDC2 activity lowers MCM3AP's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.32× higher at baseline in the lines without WFDC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[NECTIN4]] | B | NECTIN4 activity lowers MCM3AP's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.24× higher at baseline in the lines without NECTIN4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[NR3C2]] | B | NR3C2 activity lowers MCM3AP's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.27× higher at baseline in the lines without NR3C2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[HIPK2]] | B | HIPK2 activity lowers MCM3AP's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 1.31× higher at baseline in the lines without HIPK2 | 0.099 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.9, -31.6); signed map (-6.9, -41.2). **Vector** length 92.2, 21.4% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -3.4 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 3 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,235,133-46,286,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Map80, KIAA0572, GANP, SAC3 |
| Gene groups (HGNC) | Lysine acetyltransferases; Transcription and export complex 2 |
| Reactome | 4 pathways, smallest: Somatic hypermutation of immunoglobulin genes; Affinity selection of immunoglobulins; Immunoglobulin maturation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60318](https://www.uniprot.org/uniprotkb/O60318) (Germinal-center associated nuclear protein):

> [Isoform GANP]: As a component of the TREX-2 complex, involved in the export of mRNAs to the cytoplasm through the nuclear pores. Through the acetylation of histones, affects the assembly of nucleosomes at immunoglobulin variable region genes and promotes the recruitment and positioning of transcription complex to favor DNA cytosine deaminase AICDA/AID targeting, hence promoting somatic hypermutations.; [Isoform MCM3AP]: Binds to and acetylates the replication protein MCM3. Plays a role in the …

**Summary**, from NCBI Gene [8888](https://www.ncbi.nlm.nih.gov/gene/8888):

> The minichromosome maintenance protein 3 (MCM3) is one of the MCM proteins essential for the initiation of DNA replication. The protein encoded by this gene is a MCM3 binding protein. It was reported to have phosphorylation-dependent DNA-primase activity, which was up-regulated in antigen immunization induced germinal center. This protein was demonstrated to be an acetyltransferase that acetylates MCM3 and plays a role in DNA replication. The mutagenesis of a nuclear localization signal of MCM3 …

**Accessions** — [HGNC:6946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6946) · Entrez [8888](https://www.ncbi.nlm.nih.gov/gene/8888) · UniProt [O60318](https://www.uniprot.org/uniprotkb/O60318) · Ensembl [ENSG00000160294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160294)

## Data

Gene col 8334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8334); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8334]; `tensor/DDL_lfc|DDL_z.npy` [8334]; `embed/gene_vectors.npy` [8334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8334 or target_col == 8334). Every well: [[MCM3AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM3AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
