---
symbol: "PEBP4"
type: "gene"
col: 5499
ensembl_id: "ENSG00000134020"
name: "phosphatidylethanolamine binding protein 4"
location: "8p21.3"
module: 53
arm: "+"
pooled_cpm: 4.9
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PEBP4

*phosphatidylethanolamine binding protein 4* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.78× (z +30.2, q 0e+00, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.392× (z -4.6, q 0.002, down in 13 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.0516×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0664×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0857×); [[Pemetrexed (drug)]] 5 µM in 1 line (HEC-1-A 0.0898×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00393]] (+0.82, fdr 7e-06), [[DNAH10]] (+0.80, fdr 7e-06), [[L3MBTL2-AS1]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KRT86]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.78×** | +30.2 | 0e+00 | 34/38 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.65×** | +28.6 | 0e+00 | 38/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.80×** | +17.2 | 0e+00 | 5/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.94×** | +16.7 | 0e+00 | 39/42 (A-172, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.10×** | +15.2 | 0e+00 | 20/25 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.04×** | +15.1 | 0e+00 | 30/38 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.50×** | +11.3 | 2e-27 | 8/11 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.3 | 1e-18 | 27/45 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +8.1 | 3e-14 | 17/34 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +7.5 | 3e-12 | 19/38 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.9 | 5e-05 | 10/26 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.8 | 8e-05 | 11/30 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +4.7 | 1e-04 | 17/40 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.6 | 1e-04 | 13/44 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.59×** | +4.1 | 0.002 | 8/43 (A498, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 13/44 (SNU-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.005 | 11/44 (SW480, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.010 | 10/47 (A498, HT-29, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.016 | 8/44 (HCT15, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.036 | 9/43 (SW1417, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.0516×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0664×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0857×); [[Pemetrexed (drug)]] 5 µM in 1 line (HEC-1-A 0.0898×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.392×** | -4.6 | 0.002 | 13/31 (CFPAC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.70 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +15.5) | — |
| [[HEC-1-A (line)]] | alt | 6.87 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +13.1) | [[Pemetrexed (drug)]] 5 µM 0.0898× (z -8.6) |
| [[HOP62 (line)]] | alt | 3.34 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +16.0) | — |
| [[LoVo (line)]] | wt | 4.09 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 82.8× (z +20.9) | — |
| [[A-172 (line)]] | wt | 5.81 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +13.1) | — |
| [[A498 (line)]] | wt | 5.37 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 7.18 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 4.20 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.1× (z +12.9) | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0516× (z -10.6) |
| [[SW480 (line)]] | alt | 4.77 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 12.6× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.156× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 2.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 4.92 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.3× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 1.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 6.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 5.10 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.1× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +8.6) | — |
| [[SW48 (line)]] | wt | 6.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +9.2) | — |
| [[A549 (line)]] | wt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.9× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 5.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.50× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 3.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +12.2) | — |
| [[J82 (line)]] | alt | 1.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.7× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0857× (z -9.0) |
| [[SNU-423 (line)]] | alt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +8.8) | — |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | +0.82 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.80 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[L3MBTL2-AS1]] | +0.79 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[USP50]] | +0.79 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.78 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.78 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.77 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.76 | +0.81 / +0.51 | both halves | 1e-05 |  |
| [[ITGA9]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.76 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.75 | +0.74 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT86]] | B | KRT86 activity raises PEBP4's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without KRT86 | 0.008 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[IL19]] | B | IL19 activity raises PEBP4's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without IL19 | 0.016 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity raises PEBP4's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without EPHA1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises PEBP4's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FBXW10B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PEBP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DLGAP1]] | B | DLGAP1 activity lowers PEBP4's level | lines that do not express DLGAP1 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without DLGAP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZSWIM5, LINC00922; maybe low, not absent |
| [[CD96]] | B | CD96 activity raises PEBP4's level | lines that do not express CD96 (12) vs lines expressing it (38) | 1.18× lower at baseline in the lines without CD96 | 0.058 | ⚠ within organs, on part of the lines; also absent: NECTIN3, CALD1, MYLK; maybe low, not absent |
| [[FHAD1]] | B | FHAD1 activity raises PEBP4's level | lines that do not express FHAD1 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without FHAD1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, -10.0); signed map (21.9, 9.3). **Vector** length 84.3, 16.2% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +28.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +30.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +17.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +4.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylethanolamine binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,713,251-23,000,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22776, CORK1, hPEBP4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S96](https://www.uniprot.org/uniprotkb/Q96S96) (Phosphatidylethanolamine-binding protein 4):

> Promotes AKT phosphorylation, suggesting a possible role in the PI3K-AKT signaling pathway.

**Summary**, from NCBI Gene [157310](https://www.ncbi.nlm.nih.gov/gene/157310):

> The phosphatidylethanolamine (PE)-binding proteins, including PEBP4, are an evolutionarily conserved family of proteins with pivotal biologic functions, such as lipid binding and inhibition of serine proteases (Wang et al., 2004 [PubMed 15302887]).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:28319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28319) · Entrez [157310](https://www.ncbi.nlm.nih.gov/gene/157310) · UniProt [Q96S96](https://www.uniprot.org/uniprotkb/Q96S96) · Ensembl [ENSG00000134020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134020)

## Data

Gene col 5499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5499); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5499]; `tensor/DDL_lfc|DDL_z.npy` [5499]; `embed/gene_vectors.npy` [5499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5499 or target_col == 5499). Every well: [[PEBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
