---
symbol: "FBLN1"
type: "gene"
col: 1200
ensembl_id: "ENSG00000077942"
name: "fibulin 1"
location: "22q13.31"
module: 67
arm: "+"
pooled_cpm: 16.6
n_lines_expressing: 30
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# FBLN1

*fibulin 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +17.1, q 0e+00, up in 22 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 1.23× (z +3.2, q 0.099, up in 6 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HS-578T 3.49×, PANC-1 3.10×, A498 2.60×, A-172 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 2.69×, A498 2.47×, HS-578T 2.77×, A-172 2.26×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.46×; ⚠ toxic; transcription drop); [[Triamcinolone (drug)]] 5 µM in 1 line (A498 1.90×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (A498 2.41×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A498 2.31×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.410× (z -13.5, q 2e-38, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARA3]] (+0.66, fdr 1e-05), [[GGH]] (+0.62, fdr 1e-05), [[GUSB]] (+0.59, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FHL1]] → it (grade C ⚠); 3 go from it, the strongest it → [[CNPY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1200.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HS-578T 3.49×, PANC-1 3.10×, A498 2.60×, A-172 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 2.69×, A498 2.47×, HS-578T 2.77×, A-172 2.26×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.46×; ⚠ toxic; transcription drop); [[Triamcinolone (drug)]] 5 µM in 1 line (A498 1.90×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (A498 2.41×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (A498 2.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +17.1 | 0e+00 | 22/23 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +16.1 | 0e+00 | 14/16 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +11.4 | 1e-27 | 14/20 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.5 | 5e-06 | 7/18 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.34×** | +4.4 | 0.001 | 11/25 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +3.9 | 0.010 | 7/28 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.8 | 0.010 | 3/19 (Hs 766T, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.16× | +3.2 | 0.093 | 9/28 (NCI-H23, A-427, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.099 | 6/26 (A498, HOP62, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.15× | +3.1 | 0.11 | 3/28 (SW 900, PANC-1, …) | top dose only |  |
| [[DT-061 (drug)]] 5 µM |  | 1.47× | +3.1 | 0.11 | 2/25 (A-427, NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.11 | 1/27 (PANC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.11 | 4/27 (HepG2/C3A, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.410×** | -13.5 | 2e-38 | 23/27 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -9.8 | 2e-20 | 21/26 (AN3 CA, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -8.6 | 2e-15 | 15/28 (AN3 CA, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.646×** | -6.6 | 6e-09 | 16/28 (A-172, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -6.2 | 6e-08 | 15/28 (A-172, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -5.6 | 2e-06 | 12/27 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.087 | 12/27 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.087 | 8/27 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.100 | 8/26 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.750× | -3.1 | 0.11 | 3/28 (A498, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 80.5 | 7 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 5 µM 1.90× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.526× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.5) |
| [[A-172 (line)]] | wt | 79.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.0) |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.8) |
| [[HS-578T (line)]] | alt | 75.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0257× (z -22.4) |
| [[PANC-1 (line)]] | alt | 33.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.3) |
| [[A-427 (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -11.5) |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.1) |
| [[Hs 766T (line)]] | wt | 50.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.7) |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0828× (z -9.6) |
| [[SW480 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.3) |
| [[A549 (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 8.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARA3]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[GGH]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GUSB]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[P3H3]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SPC24]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PCLAF]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[NUDT1]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MMS22L]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SPC25]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[FANCI]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TP73]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHL1]] | C | FHL1 activity raises FBLN1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 4.24× lower at baseline in the lines without FHL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNPY4]] | B | FBLN1 activity raises CNPY4's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without FBLN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |
| [[MTBP]] | B | FBLN1 activity lowers MTBP's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without FBLN1 | 0.059 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |
| [[OLFML2A]] | B | FBLN1 activity raises OLFML2A's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without FBLN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.7, -39.0); signed map (-30.3, -38.3). **Vector** length 57.0, 11.5% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.4 | +3.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.2 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | fibulin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,502,238-45,601,135 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBLN |
| Gene groups (HGNC) | Fibulins |
| Hallmark sets | XENOBIOTIC_METABOLISM, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P23142](https://www.uniprot.org/uniprotkb/P23142) (Fibulin-1):

> Incorporated into fibronectin-containing matrix fibers. May play a role in cell adhesion and migration along protein fibers within the extracellular matrix (ECM). Could be important for certain developmental processes and contribute to the supramolecular organization of ECM architecture, in particular to those of basement membranes. Has been implicated in a role in cellular transformation and tumor invasion, it appears to be a tumor suppressor. May play a role in haemostasis and thrombosis …

**Summary**, from NCBI Gene [2192](https://www.ncbi.nlm.nih.gov/gene/2192):

> Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been identified among the four variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3600) · Entrez [2192](https://www.ncbi.nlm.nih.gov/gene/2192) · UniProt [P23142](https://www.uniprot.org/uniprotkb/P23142) · Ensembl [ENSG00000077942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077942)

## Data

Gene col 1200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1200); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1200]; `tensor/DDL_lfc|DDL_z.npy` [1200]; `embed/gene_vectors.npy` [1200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1200 or target_col == 1200). Every well: [[FBLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
