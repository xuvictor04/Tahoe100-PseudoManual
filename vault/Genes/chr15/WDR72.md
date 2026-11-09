---
symbol: "WDR72"
type: "gene"
col: 9301
ensembl_id: "ENSG00000166415"
name: "WD repeat domain 72"
location: "15q21.3"
module: 19
arm: "+"
pooled_cpm: 12.59
n_lines_expressing: 18
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 23
direction_downstream: 20
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# WDR72

*WD repeat domain 72* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.88× (z +15.8, q 0e+00, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +10.5, q 1e-23, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.611× (z -5.9, q 2e-06, down in 13 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H460 0.141×, CFPAC-1 0.156×, SHP-77 0.148×, A549 0.408×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.119×, NCI-H460 0.339×, CFPAC-1 0.344×); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.151×, CFPAC-1 0.134×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 0.0431×, COLO 205 0.0784×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02994]] (+0.66, fdr 7e-06), [[TARID]] (+0.64, fdr 1e-05), [[GPRIN3]] (+0.62, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[MAP2K6]] → it (grade B ⚠); 20 go from it, the strongest it → [[NDUFA4L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +15.8 | 0e+00 | 3/10 (H4, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +12.3 | 2e-32 | 1/12 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +10.8 | 9e-25 | 1/11 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +10.5 | 1e-23 | 10/16 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.0 | 2e-13 | 0/16 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.4 | 1e-08 | 7/16 (SK-MEL-2, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.2 | 2e-05 | 8/16 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 3e-05 | 7/16 (NCI-H460, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.0 | 3e-05 | 1/13 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.4 | 5e-04 | 3/15 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 7/16 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 6/16 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +4.3 | 7e-04 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 4/16 (SW1417, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 8/16 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 11/16 (NCI-H460, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.004 | 4/16 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.011 | 0/16 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.013 | 2/16 (SK-MEL-2, CFPAC-1) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.035 | 5/17 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.035 | 1/16 (SW48) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9301.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H460 0.141×, CFPAC-1 0.156×, SHP-77 0.148×, A549 0.408×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.119×, NCI-H460 0.339×, CFPAC-1 0.344×); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.151×, CFPAC-1 0.134×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 0.0431×, COLO 205 0.0784×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -5.9 | 2e-06 | 13/16 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -4.5 | 0.002 | 6/16 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.710×** | -4.0 | 0.013 | 3/16 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.763× | -3.3 | 0.15 | 13/16 (HT-29, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.767× | -3.2 | 0.15 | 5/16 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Volasertib (drug)]] 0.5 µM |  | 0.697× | -3.1 | 0.15 | 0/16 | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.757× | -3.1 | 0.15 | 1/16 (HCT15) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0482× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.9) |
| [[A549 (line)]] | wt | 134 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 46.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 62.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0813× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 15.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -9.5) |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0431× (z -14.0) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -13.9) |
| [[SW480 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -10.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A-172 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02994]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TARID]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[ENPEP]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SLC16A4]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CASC9]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PALMD]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[POF1B]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GLDN]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FRMD4B]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LINC01967]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 4, C 19. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | B | MAP2K6 activity raises WDR72's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without MAP2K6 | 0.039 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[NCKAP5]] | B | NCKAP5 activity raises WDR72's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without NCKAP5 | 0.061 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[ADD3-AS1]] | B | ADD3-AS1 activity raises WDR72's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 2.54× lower at baseline in the lines without ADD3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[PALMD]] | B | PALMD activity raises WDR72's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without PALMD | 0.077 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[F5]] | C | F5 activity raises WDR72's level | lines that do not express F5 (39) vs lines expressing it (11) | 4.43× lower at baseline in the lines without F5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[SPP1]] | C | SPP1 activity raises WDR72's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without SPP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[AKR1C2]] | C | AKR1C2 activity raises WDR72's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without AKR1C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises WDR72's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without DSCAML1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises WDR72's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 3.52× lower at baseline in the lines without GPR141 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises WDR72's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 3.67× lower at baseline in the lines without ITIH2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[POF1B]] | C | POF1B activity raises WDR72's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without POF1B | 0.029 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises WDR72's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 2.89× lower at baseline in the lines without FXYD2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 8, C 12. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFA4L2]] | B | WDR72 activity raises NDUFA4L2's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without WDR72 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[SLC16A4]] | B | WDR72 activity raises SLC16A4's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without WDR72 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[NRG4]] | B | WDR72 activity raises NRG4's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without WDR72 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[AKR1C3]] | B | WDR72 activity raises AKR1C3's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.38× lower at baseline in the lines without WDR72 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[NCKAP5]] | B | WDR72 activity raises NCKAP5's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without WDR72 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[BCL2L15]] | B | WDR72 activity raises BCL2L15's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without WDR72 | 0.021 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[CHN2]] | B | WDR72 activity raises CHN2's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.53× lower at baseline in the lines without WDR72 | 0.083 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[FAAH2]] | B | WDR72 activity strengthens FAAH2's drug response | lines that do not express WDR72 (12) vs lines expressing it (11) | the lines without WDR72 respond 0.74× as strongly (z diff +0.96); strongest at Topotecan (hydrochloride) 5 µM: 0.63x vs 0.29x (z diff +3.7) | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; target measured in part of the lines; artifact flags |
| [[AKR1C2]] | C | WDR72 activity raises AKR1C2's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.85× lower at baseline in the lines without WDR72 | 0.010 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[PEX5L]] | C | WDR72 activity raises PEX5L's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without WDR72 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[KYNU]] | C | WDR72 activity raises KYNU's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.20× lower at baseline in the lines without WDR72 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[PKHD1]] | C | WDR72 activity raises PKHD1's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.07× lower at baseline in the lines without WDR72 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.1, 43.0); signed map (46.2, 42.6). **Vector** length 54.1, 16.3% of its response variance represented; |z| ≥ 3 in 429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 72 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:53,513,741-53,762,878 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38736 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MJ13](https://www.uniprot.org/uniprotkb/Q3MJ13) (WD repeat-containing protein 72):

> Plays a major role in formation of tooth enamel. Specifically required during the maturation phase of amelogenesis for normal formation of the enamel matrix and clearance of enamel proteins. May be involved in localization of the calcium transporter SLC24A4 to the ameloblast cell membrane.

**Summary**, from NCBI Gene [256764](https://www.ncbi.nlm.nih.gov/gene/256764):

> This gene encodes a protein with eight WD-40 repeats. Mutations in this gene have been associated with amelogenesis imperfecta hypomaturation type 2A3. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:26790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26790) · Entrez [256764](https://www.ncbi.nlm.nih.gov/gene/256764) · UniProt [Q3MJ13](https://www.uniprot.org/uniprotkb/Q3MJ13) · Ensembl [ENSG00000166415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166415)

## Data

Gene col 9301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9301); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9301]; `tensor/DDL_lfc|DDL_z.npy` [9301]; `embed/gene_vectors.npy` [9301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9301 or target_col == 9301). Every well: [[WDR72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
