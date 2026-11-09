---
symbol: "C2CD6"
type: "gene"
col: 7914
ensembl_id: "ENSG00000155754"
name: "catsper channel auxiliary subunit tau"
location: "2q33.1"
module: 53
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# C2CD6

*catsper channel auxiliary subunit tau* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.89× (z +28.1, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.655× (z -4.4, q 0.006, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0938×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0672×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.119×; ⚠ cell-cycle shift, explains ~27% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.79, fdr 7e-06), [[IL12RB2]] (+0.79, fdr 7e-06), [[LINC02955]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.89×** | +28.1 | 0e+00 | 30/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +19.9 | 0e+00 | 26/35 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.26×** | +14.3 | 2e-44 | 2/4 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.51×** | +12.9 | 5e-36 | 26/42 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.12×** | +11.7 | 1e-29 | 20/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +10.5 | 6e-24 | 21/35 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +9.9 | 2e-21 | 8/20 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +9.6 | 4e-20 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +9.4 | 4e-19 | 14/46 (HS-578T, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +9.2 | 2e-18 | 15/30 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.28×** | +8.5 | 1e-15 | 23/42 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +7.8 | 3e-13 | 7/15 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +7.3 | 9e-12 | 14/45 (NCI-H1792, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +6.4 | 6e-09 | 16/45 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.9 | 2e-07 | 15/45 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.66×** | +5.2 | 6e-06 | 14/40 (NCI-H1792, SK-MEL-2, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.1 | 1e-05 | 11/38 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +4.4 | 4e-04 | 8/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.005 | 9/45 (SK-MEL-2, NCI-H2347, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0938×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0672×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.119×; ⚠ cell-cycle shift, explains ~27% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -4.4 | 0.006 | 16/43 (SK-MEL-2, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.721× | -3.4 | 0.18 | 3/42 (CFPAC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0672× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 3.01 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +14.9) | — |
| [[RPMI-7951 (line)]] | alt | 57.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0938× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.6) |
| [[LoVo (line)]] | wt | 1.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +10.2) | — |
| [[A-172 (line)]] | wt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +8.7) | — |
| [[A498 (line)]] | wt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.6) | — |
| [[SW480 (line)]] | alt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +11.6) | — |
| [[A-427 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.79 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.79 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.79 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[TG]] | +0.78 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.78 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.77 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.74 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.74 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.74 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[USP50]] | +0.73 | +0.78 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2CD6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MOB3B]] | B | MOB3B activity lowers C2CD6's level | lines that do not express MOB3B (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without MOB3B | 0.047 | ⚠ within organs, on part of the lines; also absent: MYO1D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, -9.9); signed map (22.4, 9.9). **Vector** length 60.1, 8.14% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +28.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +9.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | catsper channel auxiliary subunit tau |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,487,421-201,619,178 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25351; previously ALS2CR11, C2CD6 |
| Gene groups (HGNC) | C2 domain containing; CatSpermasome complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53TS8](https://www.uniprot.org/uniprotkb/Q53TS8) (Cation channel sperm-associated targeting subunit tau):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization. Required for CatSper complex targeting and trafficking into the quadrilinear nanodomains. Targets the preassembled CatSper complexes to elongating flagella, where it links the channel-carrying vesicles and motor proteins.

**Summary**, from NCBI Gene [151254](https://www.ncbi.nlm.nih.gov/gene/151254):

> An autosomal recessive form of juvenile amyotrophic lateral sclerosis was originally mapped to a region of chromosome 2 that includes this gene. The encoded protein contains a calcium-dependent membrane targeting C2 domain. This domain is often found in proteins that are involved in membrane trafficking and signal transduction. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:14438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14438) · Entrez [151254](https://www.ncbi.nlm.nih.gov/gene/151254) · UniProt [Q53TS8](https://www.uniprot.org/uniprotkb/Q53TS8) · Ensembl [ENSG00000155754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155754)

## Data

Gene col 7914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7914); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7914]; `tensor/DDL_lfc|DDL_z.npy` [7914]; `embed/gene_vectors.npy` [7914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7914 or target_col == 7914). Every well: [[C2CD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
