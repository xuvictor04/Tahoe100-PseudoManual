---
symbol: "RSPO3"
type: "gene"
col: 7086
ensembl_id: "ENSG00000146374"
name: "R-spondin 3"
location: "6q22.33"
module: 19
arm: "+"
pooled_cpm: 15.42
n_lines_expressing: 11
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 34
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RSPO3

*R-spondin 3* — 6q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +8.5, q 1e-14, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.99× (z +4.6, q 6e-04, up in 6 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.552× (z -4.0, q 0.039, down in 8 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 0.141×, A549 0.132×, NCI-H1573 0.149×, NCI-H2030 0.183×); [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0751×, NCI-H1573 0.0589×, A549 0.0785×; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.0465×, NCI-H460 0.143×, A549 0.120×; ⚠ cell-cycle shift, explains ~24% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H1573 0.0652×, NCI-H460 0.123×, A549 0.129×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.171×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KYNU]] (+0.74, fdr 7e-06), [[SMOC1]] (+0.69, fdr 7e-06), [[EYA2]] (+0.65, fdr 7e-06); moves opposite to [[RTN4RL1]] (-0.46, fdr 6e-05), [[ZDHHC9]] (-0.45, fdr 4e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RAB27B]] → it (grade B ⚠); 34 go from it, the strongest it → [[NR4A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +8.5 | 1e-14 | 1/7 (A549) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +7.3 | 9e-11 | 2/4 (A549, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.01×** | +6.8 | 2e-09 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +5.7 | 2e-06 | 2/7 (NCI-H1573, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +4.6 | 6e-04 | 6/8 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.8 | 0.014 | 3/7 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +3.8 | 0.014 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.034 | 0/8 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.034 | 5/8 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.036 | 2/8 (NCI-H1573, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.058 | 3/8 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.65×** | +3.2 | 0.061 | 5/8 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.080 | 4/8 (A549, SW 900, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7086.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 0.141×, A549 0.132×, NCI-H1573 0.149×, NCI-H2030 0.183×); [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0751×, NCI-H1573 0.0589×, A549 0.0785×; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.0465×, NCI-H460 0.143×, A549 0.120×; ⚠ cell-cycle shift, explains ~24% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H1573 0.0652×, NCI-H460 0.123×, A549 0.129×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.171×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -4.0 | 0.039 | 8/8 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.564× | -3.6 | 0.11 | 0/8 | inconsistent across doses |  |
| [[Brimonidine (drug)]] 0.05 µM |  | 0.612× | -3.3 | 0.18 | 1/8 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 83.4 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.92× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.0465× (z -14.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0652× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 73.2 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -15.6) |
| [[A549 (line)]] | wt | 173 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -11.9) |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0572× (z -8.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYNU]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SMOC1]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[EYA2]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[CYP24A1]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[CSGALNACT1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[PDE7B]] | +0.59 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[GSG1L2]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[UPK1B]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[TBXT]] ⚠ | +0.57 | +0.56 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GLP2R]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[EBF1]] | +0.56 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[SEMA3C]] | +0.55 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[EYA4]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN4RL1]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ZDHHC9]] | -0.45 | -0.26 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB27B]] | B | RAB27B activity raises RSPO3's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without RAB27B | 0.071 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[EBF1]] | C | EBF1 activity raises RSPO3's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without EBF1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[F2RL2]] | C | F2RL2 activity raises RSPO3's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 3.50× lower at baseline in the lines without F2RL2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |
| [[UPK1B]] | C | UPK1B activity raises RSPO3's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 4.32× lower at baseline in the lines without UPK1B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |
| [[CPS1]] | C | CPS1 activity raises RSPO3's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 3.87× lower at baseline in the lines without CPS1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R; co-absent with the target |
| [[SERPINE2]] | C | SERPINE2 activity raises RSPO3's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without SERPINE2 | 0.031 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12; co-absent with the target |
| [[CRLF2]] | C | CRLF2 activity raises RSPO3's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 5.02× lower at baseline in the lines without CRLF2 | 0.033 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[HORMAD1]] | C | HORMAD1 activity raises RSPO3's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without HORMAD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises RSPO3's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without KYNU | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[P3H2-AS1]] | C | P3H2-AS1 activity raises RSPO3's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without P3H2-AS1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises RSPO3's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 5.55× lower at baseline in the lines without GLP2R | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 27, C 7. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A3]] | B | RSPO3 activity raises NR4A3's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 3.19× lower at baseline in the lines without RSPO3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[MAP3K20]] | B | RSPO3 activity raises MAP3K20's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without RSPO3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[SLC16A2]] | B | RSPO3 activity raises SLC16A2's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 2.76× lower at baseline in the lines without RSPO3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Methylthiouracil (drug)]] 0.05 µM | B | RSPO3 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.81× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM | B | RSPO3 activity raises the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.86× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | RSPO3 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.76× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[XRK3F2 (drug)]] 5 µM | B | RSPO3 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[AZD2858 (drug)]] 0.5 µM | B | RSPO3 activity raises the cells' numbers under AZD2858 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 0.5 µM | B | RSPO3 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Fulvestrant (drug)]] 5 µM | B | RSPO3 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Pioglitazone (drug)]] 0.5 µM | B | RSPO3 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.27× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | RSPO3 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.20× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 33.0); signed map (38.9, 46.0). **Vector** length 46.0, 19.9% of its response variance represented; |z| ≥ 3 in 283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +0.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.0 | +2.4 |
|  | [[Thymol (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | R-spondin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.33 — chr6:127,118,671-127,199,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14440; previously THSD2 |
| Gene groups (HGNC) | R-spondin family |
| Reactome | 5 pathways, smallest: RUNX1 regulates transcription of genes involved in WNT signaling; Regulation of FZD by ubiquitination; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXY4](https://www.uniprot.org/uniprotkb/Q9BXY4) (R-spondin-3):

> Activator of the canonical Wnt signaling pathway by acting as a ligand for LGR4-6 receptors, which acts as a key regulator of angiogenesis. Upon binding to LGR4-6 (LGR4, LGR5 or LGR6), LGR4-6 associate with phosphorylated LRP6 and frizzled receptors that are activated by extracellular Wnt receptors, triggering the canonical Wnt signaling pathway to increase expression of target genes. Also regulates the canonical Wnt/beta-catenin-dependent pathway and non-canonical Wnt signaling by acting as an …

**Summary**, from NCBI Gene [84870](https://www.ncbi.nlm.nih.gov/gene/84870):

> This gene belongs to the R-spondin family. The encoded protein plays a role in the regulation of Wnt (wingless-type MMTV integration site family)/beta-catenin and Wnt/planar cell polarity (PCP) signaling pathways, which are involved in development, cell growth and disease pathogenesis. Genome-wide association studies suggest a correlation of this gene with bone mineral density and risk of fracture. This gene may be involved in tumor development. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:20866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20866) · Entrez [84870](https://www.ncbi.nlm.nih.gov/gene/84870) · UniProt [Q9BXY4](https://www.uniprot.org/uniprotkb/Q9BXY4) · Ensembl [ENSG00000146374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146374)

## Data

Gene col 7086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7086); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7086]; `tensor/DDL_lfc|DDL_z.npy` [7086]; `embed/gene_vectors.npy` [7086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7086 or target_col == 7086). Every well: [[RSPO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSPO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
