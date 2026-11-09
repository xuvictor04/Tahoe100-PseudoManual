---
symbol: "TARID"
type: "gene"
col: 13615
ensembl_id: "ENSG00000227954"
name: "TCF21 antisense RNA inducing promoter demethylation"
location: "6q23.2"
module: 19
arm: "+"
pooled_cpm: 17.79
n_lines_expressing: 21
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 20
direction_downstream: 20
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TARID

*TCF21 antisense RNA inducing promoter demethylation* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +22.0, q 0e+00, up in 5 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.719× (z -4.4, q 0.008, down in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Glycyrrhizic acid (drug)]] 5 µM: 0.741× (z -3.8, q 0.040, down in 1 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.0785×, NCI-H1792 0.151×, SNU-423 0.0994×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.120×, HT-29 0.133×; ⚠ cell-cycle shift, explains ~16% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SHP-77 0.152×, COLO 205 0.228×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.257×, A549 0.213×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.318×, SHP-77 0.370×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PON3]] (+0.66, fdr 1e-05), [[XDH]] (+0.65, fdr 7e-06), [[WDR72]] (+0.64, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[SIPA1L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +22.0 | 0e+00 | 5/19 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +15.7 | 0e+00 | 12/19 (SW1417, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +13.2 | 2e-37 | 6/17 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.7 | 2e-29 | 2/13 (NCI-H2347, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +9.5 | 3e-19 | 1/14 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +9.2 | 2e-18 | 10/18 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +9.1 | 1e-17 | 14/18 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +8.6 | 4e-16 | 5/18 (CFPAC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.6 | 3e-12 | 4/18 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.1 | 8e-11 | 8/19 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.8 | 6e-10 | 5/19 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +5.5 | 2e-06 | 6/18 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +5.2 | 1e-05 | 6/18 (SNU-423, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 3e-04 | 6/17 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 3/18 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.004 | 4/18 (SW1417, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.028 | 2/18 (SW1417, NCI-H1573) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.0 | 0.072 | 3/18 (NCI-H460, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.0785×, NCI-H1792 0.151×, SNU-423 0.0994×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.120×, HT-29 0.133×; ⚠ cell-cycle shift, explains ~16% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SHP-77 0.152×, COLO 205 0.228×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.257×, A549 0.213×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.318×, SHP-77 0.370×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -4.4 | 0.008 | 15/18 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.040 | 1/18 (NCI-H1573) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.836× | -3.3 | 0.12 | 11/20 (CFPAC-1, NCI-H2122, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.777× | -3.3 | 0.12 | 6/18 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.787× | -3.2 | 0.18 | 1/18 (SNU-423) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.851× | -3.0 | 0.22 | 0/20 | top dose only | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.22 | 1/19 (SNU-423) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 106 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.228× (z -8.5) |
| [[SHP-77 (line)]] | alt | 62.2 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.152× (z -12.1) |
| [[A549 (line)]] | wt | 52.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0785× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.5) |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -9.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 40.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.81× (z +9.9) | — |
| [[A-172 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PON3]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[XDH]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[WDR72]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[HORMAD1]] | +0.63 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.62 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ENPEP]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ITIH2]] | +0.58 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[IGFBP1]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[CYP24A1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SMOC1]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ST6GAL2]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[HAVCR1]] | +0.53 | +0.51 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FLRT3]] | B | FLRT3 activity raises TARID's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without FLRT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[NCKAP5]] | B | NCKAP5 activity raises TARID's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without NCKAP5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[LINC02284]] | B | LINC02284 activity raises TARID's level | lines that do not express LINC02284 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without LINC02284 | 0.097 | ⚠ within organs, on part of the lines; also absent: PELI2, CFH, ADAM28; maybe low, not absent |
| [[SIPA1L2]] | B | SIPA1L2 activity raises TARID's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without SIPA1L2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[NTN4]] | C | NTN4 activity raises TARID's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without NTN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2; co-absent with the target |
| [[FGA]] | C | FGA activity raises TARID's level | lines that do not express FGA (43) vs lines expressing it (7) | 6.07× lower at baseline in the lines without FGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises TARID's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without GPRIN3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[PDK4]] | C | PDK4 activity raises TARID's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 3.02× lower at baseline in the lines without PDK4 | 0.023 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises TARID's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.87× lower at baseline in the lines without STEAP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises TARID's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 3.46× lower at baseline in the lines without IGFBP1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[GDA]] | C | GDA activity raises TARID's level | lines that do not express GDA (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without GDA | 0.042 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 12, C 8. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIPA1L2]] | B | TARID activity raises SIPA1L2's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TARID | 0.018 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[LINC02889]] | B | TARID activity raises LINC02889's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without TARID | 0.032 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[NCKAP5]] | B | TARID activity raises NCKAP5's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TARID | 0.046 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[BCL2L15]] | B | TARID activity raises BCL2L15's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without TARID | 0.060 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| cells under [[Trifluridine (drug)]] 5 µM | B | TARID activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TARID (29) vs lines expressing it (19) | the lines without TARID: 0.92× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[ARSL]] | B | TARID activity raises ARSL's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without TARID | 0.073 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[GPR37]] | B | TARID activity raises GPR37's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without TARID | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[LINC02284]] | B | TARID activity raises LINC02284's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TARID | 0.090 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[SQOR]] | B | TARID activity raises SQOR's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without TARID | 0.090 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | TARID activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express TARID (29) vs lines expressing it (19) | the lines without TARID: 1.13× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| cells under [[Rimonabant (drug)]] 5 µM | B | TARID activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express TARID (29) vs lines expressing it (19) | the lines without TARID: 1.10× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[GSAP]] | B | TARID activity raises GSAP's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TARID | 0.095 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.9, 43.5); signed map (46.4, 42.5). **Vector** length 56.1, 16.2% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.7 | +1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | TCF21 antisense RNA inducing promoter demethylation |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q23.2 — chr6:133,502,252-133,892,802 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously EYA4-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50506) · Entrez [100507308](https://www.ncbi.nlm.nih.gov/gene/100507308) · Ensembl [ENSG00000227954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227954)

## Data

Gene col 13615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13615); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13615]; `tensor/DDL_lfc|DDL_z.npy` [13615]; `embed/gene_vectors.npy` [13615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13615 or target_col == 13615). Every well: [[TARID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
