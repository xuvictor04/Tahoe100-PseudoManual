---
symbol: "PCCA-DT"
type: "gene"
col: 15827
ensembl_id: "ENSG00000274605"
name: "PCCA divergent transcript"
location: "13q32.3"
module: 125
arm: "+"
pooled_cpm: 6.51
n_lines_expressing: 49
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PCCA-DT

*PCCA divergent transcript* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.85× (z +16.9, q 0e+00, up in 46 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 5 µM in 1 line (NCI-H23 0.106×; ⚠ toxic); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (RKO 0.0553×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEH1-DT]] (+0.58, fdr 1e-05), [[CEBPB]] (+0.56, fdr 1e-05), [[UPP1]] (+0.50, fdr 3e-04); moves opposite to [[KNTC1]] (-0.42, fdr 4e-04), [[FANCG]] (-0.42, fdr 1e-04), [[RBBP7]] (-0.41, fdr 2e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.85×** | +16.9 | 0e+00 | 46/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +16.4 | 0e+00 | 38/40 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.48×** | +16.3 | 0e+00 | 45/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.14×** | +13.6 | 6e-40 | 44/46 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +10.7 | 1e-24 | 26/39 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.72×** | +9.6 | 1e-19 | 22/29 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +9.2 | 2e-18 | 38/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.99×** | +9.2 | 3e-18 | 9/10 (BT-474, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **2.52×** | +7.8 | 5e-13 | 22/30 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +7.7 | 9e-13 | 31/46 (SW480, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +7.1 | 9e-11 | 28/46 (SNU-423, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +6.8 | 7e-10 | 23/45 (SW1417, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +6.7 | 9e-10 | 27/44 (J82, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.98×** | +6.5 | 3e-09 | 24/42 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.07×** | +6.4 | 6e-09 | 12/18 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.2 | 2e-08 | 20/39 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.81×** | +5.6 | 6e-07 | 22/46 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.63×** | +4.6 | 1e-04 | 14/46 (SW480, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.52×** | +4.6 | 1e-04 | 19/44 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 3e-04 | 16/45 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~25% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 5 µM in 1 line (NCI-H23 0.106×; ⚠ toxic); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (RKO 0.0553×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +14.3) | — |
| [[A498 (line)]] | wt | 7.14 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.95× (z +10.8) | — |
| [[J82 (line)]] | alt | 6.94 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +11.0) | — |
| [[A-172 (line)]] | wt | 6.86 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 7.77 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.48× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.29 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.0× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 4.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 17.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.85× (z +8.8) | — |
| [[LoVo (line)]] | wt | 10.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 7.01 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.106× (z -9.2) ⚠ toxic |
| [[RKO (line)]] | wt | 4.53 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0553× (z -9.0) |
| [[A-427 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEH1-DT]] | +0.58 | +0.69 / +0.51 | both halves | 1e-05 | same gene group |
| [[CEBPB]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[UPP1]] | +0.50 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[VHL]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[INSYN2A]] | +0.49 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[EVI2B]] | +0.49 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[HRK]] | +0.47 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[ZNF232-AS1]] | +0.47 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[TMEM251]] | +0.47 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NOS1]] | +0.47 | +0.32 / +0.47 | both halves | 1e-04 |  |
| [[NPL]] | +0.46 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.46 | +0.38 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNTC1]] | -0.42 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[FANCG]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[RBBP7]] | -0.41 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[PHTF2]] | -0.41 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[CALM3]] | -0.40 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ADAM15]] | -0.40 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ADD3]] | -0.40 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[NCAPD3]] | -0.39 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity lowers PCCA-DT's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.80× higher at baseline in the lines without G0S2 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[ROBO3]] | B | ROBO3 activity lowers PCCA-DT's level | lines that do not express ROBO3 (8) vs lines expressing it (42) | 1.93× higher at baseline in the lines without ROBO3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, DYRK3, SCHIP1 |
| [[TOP2A]] | B | TOP2A activity lowers PCCA-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CSF3]] | B | CSF3 activity lowers PCCA-DT's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.67× higher at baseline in the lines without CSF3 | 0.084 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[HOMER3]] | C | HOMER3 activity lowers PCCA-DT's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.65× higher at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.422). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 12.9); signed map (14.2, 29.7). **Vector** length 51.7, 7.34% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +3.1 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.0 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Pentagastrin (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PCCA divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q32.3 — chr13:100,053,074-100,088,972 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53266) · Entrez [105370333](https://www.ncbi.nlm.nih.gov/gene/105370333) · Ensembl [ENSG00000274605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274605)

## Data

Gene col 15827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15827); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15827]; `tensor/DDL_lfc|DDL_z.npy` [15827]; `embed/gene_vectors.npy` [15827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15827 or target_col == 15827). Every well: [[PCCA-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCCA-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
