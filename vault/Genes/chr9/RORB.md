---
symbol: "RORB"
type: "gene"
col: 12759
ensembl_id: "ENSG00000198963"
name: "RAR related orphan receptor B"
location: "9q21.13"
module: 9
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 23
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# RORB

*RAR related orphan receptor B* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.74× (z +23.6, q 0e+00, up in 11 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.171×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.194×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.161×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.266×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 900 0.143×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH17]] (+0.72, fdr 7e-06), [[PCDH10]] (+0.63, fdr 1e-05), [[TCIM]] (+0.62, fdr 3e-05); moves opposite to [[NUDCD3]] (-0.45, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[MCC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.74×** | +23.6 | 0e+00 | 11/16 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **8.41×** | +20.4 | 0e+00 | 16/19 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.93×** | +18.5 | 0e+00 | 16/19 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +18.5 | 0e+00 | 11/16 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **6.03×** | +17.2 | 0e+00 | 15/19 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.07×** | +15.1 | 0e+00 | 14/19 (J82, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.82×** | +12.8 | 1e-35 | 17/19 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.65×** | +11.9 | 9e-31 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.33×** | +11.0 | 2e-26 | 13/18 (J82, A498, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +8.4 | 2e-15 | 9/17 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +8.2 | 1e-14 | 1/7 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +7.5 | 2e-12 | 7/16 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +7.2 | 2e-11 | 6/15 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +7.0 | 1e-10 | 8/15 (HOP62, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.05×** | +6.8 | 3e-10 | 8/14 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.46×** | +6.2 | 2e-08 | 10/16 (J82, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.9 | 1e-07 | 7/14 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12759.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.171×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.194×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.161×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.266×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW 900 0.143×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.3 | 0.23 | 1/19 (HOP62) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.795× | -3.2 | 0.23 | 2/19 (LOX-IMVI, C32) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.797× | -3.2 | 0.23 | 10/19 (NCI-H1792, H4, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.705× | -3.2 | 0.23 | 1/19 (NCI-H23) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.40 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.9× (z +12.8) | — |
| [[J82 (line)]] | alt | 15.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +16.8) | — |
| [[A498 (line)]] | wt | 12.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 3.74 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 17.7× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 2.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 2.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 1.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.8× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.143× (z -8.5) |
| [[A-172 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.796 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.588 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH17]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[PCDH10]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TCIM]] | +0.62 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[TMEFF2]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[DMD]] | +0.58 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[TP63]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[EPHA7]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[BMP2]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[NRXN1]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[HMCN1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ATP1B1]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDCD3]] | -0.45 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RORB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENPP2]] | C | ENPP2 activity raises RORB's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without ENPP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[SLIT2]] | C | SLIT2 activity raises RORB's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without SLIT2 | 0.043 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises RORB's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without PEX5L | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[LINC02360]] | C | LINC02360 activity raises RORB's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 1.46× lower at baseline in the lines without LINC02360 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCC]] | B | RORB activity raises MCC's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without RORB | 0.077 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent |
| [[KCNT2]] | C | RORB activity raises KCNT2's level | lines that do not express RORB (27) vs lines expressing it (23) | 4.16× lower at baseline in the lines without RORB | 0.036 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[PDLIM3]] | C | RORB activity raises PDLIM3's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without RORB | 0.045 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[ADAM28]] | C | RORB activity raises ADAM28's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without RORB | 0.058 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[NOVA1]] | C | RORB activity raises NOVA1's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without RORB | 0.073 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 30.1); signed map (37.9, 30.8). **Vector** length 48.7, 11.1% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +23.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.7 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RAR related orphan receptor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:74,497,335-74,693,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RZRB, NR1F2, ROR-BETA, RORβ, RZR-BETA |
| Gene groups (HGNC) | RAR related orphan receptors |
| Reactome | 3 pathways, smallest: Expression of BMAL (ARNTL), CLOCK, and NPAS2; Nuclear Receptor transcription pathway; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92753](https://www.uniprot.org/uniprotkb/Q92753) (Nuclear receptor ROR-beta):

> Nuclear receptor that binds DNA as a monomer to ROR response elements (RORE) containing a single core motif half-site 5'-AGGTCA-3' preceded by a short A-T-rich sequence. Considered to have intrinsic transcriptional activity, have some natural ligands such as all-trans retinoic acid (ATRA) and other retinoids which act as inverse agonists repressing the transcriptional activity. Required for normal postnatal development of rod and cone photoreceptor cells. Modulates rod photoreceptors …

**Summary**, from NCBI Gene [6096](https://www.ncbi.nlm.nih.gov/gene/6096):

> The protein encoded by this gene is a member of the NR1 subfamily of nuclear hormone receptors. It is a DNA-binding protein that can bind as a monomer or as a homodimer to hormone response elements upstream of several genes to enhance the expression of those genes. The encoded protein has been shown to interact with NM23-2, a nucleoside diphosphate kinase involved in organogenesis and differentiation, and to help regulate the expression of some genes involved in circadian rhythm. [provided by …

**Accessions** — [HGNC:10259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10259) · Entrez [6096](https://www.ncbi.nlm.nih.gov/gene/6096) · UniProt [Q92753](https://www.uniprot.org/uniprotkb/Q92753) · Ensembl [ENSG00000198963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198963)

## Data

Gene col 12759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12759); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12759]; `tensor/DDL_lfc|DDL_z.npy` [12759]; `embed/gene_vectors.npy` [12759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12759 or target_col == 12759). Every well: [[RORB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RORB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
