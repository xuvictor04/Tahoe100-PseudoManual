---
symbol: "PAX7"
type: "gene"
col: 189
ensembl_id: "ENSG00000009709"
name: "paired box 7"
location: "1p36.13"
module: 19
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 15
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PAX7

*paired box 7* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.82× (z +13.8, q 8e-41, up in 2 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.112×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0738×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0852×); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.117×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A5]] (+0.90, fdr 7e-06), [[SCARA5]] (+0.89, fdr 7e-06), [[GLP2R]] (+0.86, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SLITRK4]] → it (grade C ⚠); 8 go from it, the strongest it → [[MN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.82×** | +13.8 | 8e-41 | 2/6 (A549, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.80×** | +10.9 | 2e-25 | 1/2 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.24×** | +9.9 | 7e-21 | 1/2 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.02×** | +9.3 | 2e-18 | 0/2 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +5.4 | 1e-05 | 1/7 (BT-474) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.7 | 2e-04 | 0/4 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.6 | 4e-04 | 3/10 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +4.2 | 0.002 | 4/7 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.52×** | +4.1 | 0.003 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.1 | 0.003 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.89×** | +4.0 | 0.004 | 2/6 (A549, Hs 766T) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.8 | 0.008 | 1/3 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +3.6 | 0.012 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +3.5 | 0.019 | 0/5 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.025 | 0/6 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.13×** | +3.4 | 0.027 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +3.3 | 0.028 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.031 | 2/10 (NCI-H460, A549) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.048 | 1/8 (NCI-H1573) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.050 | 0/8 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.1 | 0.050 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.112×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0738×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0852×); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 0.117×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.605× | -3.1 | 0.67 | 2/10 (HS-578T, NCI-H1573) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.595× | -3.0 | 0.67 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -15.4) |
| [[A-172 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.784 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.625 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.893 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A5]] | +0.90 | +0.92 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.89 | +0.88 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.86 | +0.84 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.85 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PDE1A]] | +0.83 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.83 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[LIN7A]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[GREM2]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLITRK4]] | C | SLITRK4 activity raises PAX7's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without SLITRK4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises PAX7's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.67× lower at baseline in the lines without SLC15A5 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises PAX7's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.26× lower at baseline in the lines without GTF2I-AS1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises PAX7's level | lines that do not express TBXT (47) vs lines expressing it (3) | 4.98× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[GSG1L2]] | C | GSG1L2 activity raises PAX7's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.77× lower at baseline in the lines without GSG1L2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises PAX7's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.40× lower at baseline in the lines without MARCOL, SPINK13 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[CDH11]] | C | CDH11 activity raises PAX7's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without CDH11 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises PAX7's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.90× lower at baseline in the lines without CTNND2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises PAX7's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.69× lower at baseline in the lines without AKR1B10 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises PAX7's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without NLGN4Y | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises PAX7's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.57× lower at baseline in the lines without C5orf46 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MN1]] | B | PAX7 activity raises MN1's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without PAX7 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent |
| [[SLC16A4]] | B | PAX7 activity raises SLC16A4's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 1.56× lower at baseline in the lines without PAX7 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent |
| [[CNTN1]] | C | PAX7 activity raises CNTN1's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.90× lower at baseline in the lines without PAX7 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[COL4A6]] | C | PAX7 activity raises COL4A6's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without PAX7 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[WDR72]] | C | PAX7 activity raises WDR72's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without PAX7 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[MEIOB]] | C | PAX7 activity raises MEIOB's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 1.64× lower at baseline in the lines without PAX7 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | PAX7 activity raises CTNND2's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.54× lower at baseline in the lines without PAX7 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[CAVIN2]] | C | PAX7 activity raises CAVIN2's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without PAX7 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 36.3); signed map (43.2, 44.0). **Vector** length 34.0, 12.2% of its response variance represented; |z| ≥ 3 in 253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | paired box 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:18,630,846-18,748,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hup1 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes |
| Reactome | 2 pathways, smallest: Specification of the neural plate border; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23759](https://www.uniprot.org/uniprotkb/P23759) (Paired box protein Pax-7):

> Transcription factor that is involved in the regulation of muscle stem cells proliferation, playing a role in myogenesis and muscle regeneration.

**Summary**, from NCBI Gene [5081](https://www.ncbi.nlm.nih.gov/gene/5081):

> This gene is a member of the paired box (PAX) family of transcription factors. Members of this gene family typically contain a paired box domain, an octapeptide, and a paired-type homeodomain. These genes play critical roles during fetal development and cancer growth. The specific function of the paired box 7 gene is unknown but speculated to involve tumor suppression since fusion of this gene with a forkhead domain family member has been associated with alveolar rhabdomyosarcoma. Three …

**Accessions** — [HGNC:8621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8621) · Entrez [5081](https://www.ncbi.nlm.nih.gov/gene/5081) · UniProt [P23759](https://www.uniprot.org/uniprotkb/P23759) · Ensembl [ENSG00000009709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009709)

## Data

Gene col 189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 189); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 189]; `tensor/DDL_lfc|DDL_z.npy` [189]; `embed/gene_vectors.npy` [189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 189 or target_col == 189). Every well: [[PAX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
