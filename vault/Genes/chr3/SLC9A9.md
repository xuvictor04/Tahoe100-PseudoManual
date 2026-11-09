---
symbol: "SLC9A9"
type: "gene"
col: 11214
ensembl_id: "ENSG00000181804"
name: "solute carrier family 9 member A9"
location: "3q24"
module: 90
arm: "+"
pooled_cpm: 6.27
n_lines_expressing: 45
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 34
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# SLC9A9

*solute carrier family 9 member A9* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.10× (z +21.6, q 0e+00, up in 29 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1792 0.0575×, CHP-212 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (CHP-212 0.0427×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.511×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (H4 0.0610×); [[Talc (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0518×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO2B1]] (+0.71, fdr 7e-06), [[LINC00871]] (+0.65, fdr 7e-06), [[GPM6A]] (+0.64, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PEX5L]] → it (grade B ⚠); 1 goes from it, the strongest it → [[STAT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.10×** | +21.6 | 0e+00 | 29/35 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.37×** | +19.5 | 0e+00 | 28/32 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.88×** | +14.0 | 4e-42 | 33/41 (SW480, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +11.9 | 1e-30 | 6/10 (H4, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +11.3 | 3e-27 | 7/17 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.22×** | +10.1 | 5e-22 | 4/11 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.82×** | +9.7 | 3e-20 | 32/40 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.94×** | +9.4 | 4e-19 | 27/40 (HS-578T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.55×** | +8.7 | 1e-16 | 24/32 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.49×** | +8.5 | 1e-15 | 28/38 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +6.7 | 9e-10 | 18/40 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.02×** | +6.6 | 3e-09 | 21/39 (A-172, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 5e-09 | 19/41 (A-172, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +6.4 | 7e-09 | 21/40 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +6.3 | 9e-09 | 21/39 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.3 | 1e-08 | 10/28 (SW 900, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.93×** | +5.9 | 1e-07 | 17/38 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +5.7 | 4e-07 | 17/35 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1792 0.0575×, CHP-212 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (CHP-212 0.0427×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 0.511×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (H4 0.0610×); [[Talc (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0518×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.672× | -3.5 | 0.13 | 11/41 (CHP-212, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.698× | -3.4 | 0.13 | 16/39 (H4, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.700× | -3.4 | 0.13 | 14/40 (A498, CHP-212, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.712× | -3.2 | 0.17 | 5/39 (SW 1088, CHP-212, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.18 | 14/35 (HOP62, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.799× | -3.0 | 0.18 | 5/41 (KATO III, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.728× | -3.0 | 0.18 | 15/38 (CHP-212, H4, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.56 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 44.8× (z +20.2) | — |
| [[SW480 (line)]] | alt | 1.92 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +15.3) | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0427× (z -10.2) |
| [[J82 (line)]] | alt | 4.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 9.38 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +14.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0951× (z -8.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H1573 (line)]] | alt | 3.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.6× (z +16.0) | — |
| [[A549 (line)]] | wt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +8.6) | — |
| [[C32 (line)]] | wt | 2.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.8× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +10.8) | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0610× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 4.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 8.50 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.511× (z -9.3) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0518× (z -8.5) |
| [[LoVo (line)]] | wt | 2.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 4.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.71× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[NCI-H23 (line)]] | alt | 3.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.6× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.81 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0676× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0774× (z -8.7) ⚠ transcription drop; unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 9.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.2) | — |
| [[A-427 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO2B1]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[LINC00871]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[GPM6A]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EGFEM1P]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[PEX5L]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[IPCEF1]] | +0.62 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[SYNPO2]] | +0.61 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MYO16]] | +0.61 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[CFAP54]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[THSD7B]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEX5L]] | B | PEX5L activity raises SLC9A9's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without PEX5L | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[KCNT2]] | B | KCNT2 activity raises SLC9A9's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.47× lower at baseline in the lines without KCNT2 | 0.003 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1 |
| [[PHACTR1]] | B | PHACTR1 activity raises SLC9A9's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without PHACTR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[SPOCK3]] | B | SPOCK3 activity raises SLC9A9's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without SPOCK3 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[ADAMTS3]] | B | ADAMTS3 activity raises SLC9A9's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without ADAMTS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949 |
| [[TOP2A]] | B | TOP2A activity lowers SLC9A9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EGF]] | B | EGF activity raises SLC9A9's level | lines that do not express EGF (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without EGF | 0.051 | ⚠ within organs, on part of the lines; also absent: LNX1, LAMB4, GNAS-AS1 |
| [[PRKG1]] | B | PRKG1 activity raises SLC9A9's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without PRKG1 | 0.064 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT4]] | B | SLC9A9 activity raises STAT4's level | lines that do not express SLC9A9 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without SLC9A9 | 0.077 | ⚠ within organs, on part of the lines; also absent: CNN3, SLC35F1, HACE1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, 29.3); signed map (34.7, 16.9). **Vector** length 70.0, 12.3% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +21.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +19.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | +6.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | +6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | +6.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:143,265,222-143,848,485 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35613, NHE9 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 6 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVB4](https://www.uniprot.org/uniprotkb/Q8IVB4) (Sodium/hydrogen exchanger 9):

> Endosomal Na(+), K(+)/H(+) antiporter. Mediates the electroneutral exchange of endosomal luminal H(+) for a cytosolic Na(+) or K(+) (Probable). By facilitating proton efflux, SLC9A9 counteracts the acidity generated by vacuolar (V)-ATPase, thereby limiting luminal acidification. Regulates organellar pH and consequently, e.g., endosome maturation and endocytic trafficking of plasma membrane receptors and neurotransporters. Promotes the recycling of transferrin receptors back to the cell surface …

**Summary**, from NCBI Gene [285195](https://www.ncbi.nlm.nih.gov/gene/285195):

> This gene encodes a sodium/proton exchanger that is a member of the solute carrier 9 protein family. The encoded protein localizes the to the late recycling endosomes and may play an important role in maintaining cation homeostasis. Mutations in this gene are associated with autism susceptibility 16 and attention-deficit/hyperactivity disorder. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:20653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20653) · Entrez [285195](https://www.ncbi.nlm.nih.gov/gene/285195) · UniProt [Q8IVB4](https://www.uniprot.org/uniprotkb/Q8IVB4) · Ensembl [ENSG00000181804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181804)

## Data

Gene col 11214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11214); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11214]; `tensor/DDL_lfc|DDL_z.npy` [11214]; `embed/gene_vectors.npy` [11214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11214 or target_col == 11214). Every well: [[SLC9A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
