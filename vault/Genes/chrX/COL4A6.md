---
symbol: "COL4A6"
type: "gene"
col: 12419
ensembl_id: "ENSG00000197565"
name: "collagen type IV alpha 6 chain"
location: "Xq22.3"
module: 19
arm: "+"
pooled_cpm: 43.38
n_lines_expressing: 14
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 25
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# COL4A6

*collagen type IV alpha 6 chain* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +10.5, q 3e-23, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +7.5, q 9e-12, up in 1 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.620× (z -3.7, q 0.080, down in 2 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GREM2]] (+0.85, fdr 7e-06), [[LINC03000]] (+0.83, fdr 7e-06), [[KCNK2]] (+0.80, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[BMPER]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +10.5 | 3e-23 | 4/9 (Panc 03.27, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +8.6 | 3e-15 | 4/9 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +7.5 | 9e-12 | 1/12 (NCI-H661) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.2 | 1e-10 | 0/8 | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.5 | 4e-06 | 7/12 (Panc 03.27, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.9 | 1e-04 | 7/12 (HOP62, Hs 766T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.1 | 0.004 | 1/6 (A549) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.023 | 1/12 (NCI-H661) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.053 | 6/12 (Panc 03.27, NCI-H460, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.069 | 3/11 (Panc 03.27, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.620×** | -3.7 | 0.080 | 2/11 (CHP-212, NCI-H460) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.653×** | -3.6 | 0.080 | 1/10 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.742×** | -3.5 | 0.080 | 1/12 (CHP-212) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -3.4 | 0.080 | 7/12 (NCI-H460, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 187 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 685 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -15.2) |
| [[A549 (line)]] | wt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.6) |
| [[Hs 766T (line)]] | wt | 54.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.2) |
| [[A-172 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GREM2]] | +0.85 | +0.87 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CDH11]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[PDE7B]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NCKAP5-AS2]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 2, C 23. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL4A6's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BMPER]] | B | BMPER activity raises COL4A6's level | lines that do not express BMPER (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without BMPER | 0.063 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[C5orf46]] | C | C5orf46 activity raises COL4A6's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without C5orf46 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises COL4A6's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.64× lower at baseline in the lines without PDCD1LG2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[COL4A5]] | C | COL4A5 activity raises COL4A6's level | lines that do not express COL4A5 (26) vs lines expressing it (24) | 3.61× lower at baseline in the lines without COL4A5 | 0.029 | ⚠ within organs, on part of the lines; also absent: COL4A6, ADAM23, GJA1; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises COL4A6's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without TNFRSF11B | 0.031 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[GJA1]] | C | GJA1 activity raises COL4A6's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without GJA1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises COL4A6's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ALPK2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises COL4A6's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.58× lower at baseline in the lines without SIRLNT | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[PAX7]] | C | PAX7 activity raises COL4A6's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without PAX7 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises COL4A6's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without PDE3A | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises COL4A6's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.55× lower at baseline in the lines without GTF2I-AS1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | COL4A6 activity raises BMPER's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without COL4A6 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035 |
| [[COL4A5]] | C | COL4A6 activity raises COL4A5's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 6.08× lower at baseline in the lines without COL4A6 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[TENM2]] | C | COL4A6 activity raises TENM2's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without COL4A6 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[MN1]] | C | COL4A6 activity raises MN1's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL4A6 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[CPED1]] | C | COL4A6 activity raises CPED1's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 1.84× lower at baseline in the lines without COL4A6 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[FST]] | C | COL4A6 activity raises FST's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 4.11× lower at baseline in the lines without COL4A6 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PDCD1LG2]] | C | COL4A6 activity raises PDCD1LG2's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 1.71× lower at baseline in the lines without COL4A6 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PDE3A]] | C | COL4A6 activity raises PDE3A's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 4.55× lower at baseline in the lines without COL4A6 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[SOX7]] | C | COL4A6 activity raises SOX7's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.98× lower at baseline in the lines without COL4A6 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[GNG11]] | C | COL4A6 activity raises GNG11's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL4A6 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 35.6); signed map (42.3, 44.0). **Vector** length 42.4, 16.0% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.54 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 6 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:108,155,607-108,439,497 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Network forming collagens |
| Reactome | 25 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Fibronectin matrix formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14031](https://www.uniprot.org/uniprotkb/Q14031) (Collagen alpha-6(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.

**Summary**, from NCBI Gene [1288](https://www.ncbi.nlm.nih.gov/gene/1288):

> This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene, alpha 5 type IV collagen, so that the gene pair shares a common promoter. Deletions in the alpha 5 gene that extend into the alpha 6 gene result in diffuse leiomyomatosis accompanying the X-linked Alport syndrome caused by the …

**Accessions** — [HGNC:2208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2208) · Entrez [1288](https://www.ncbi.nlm.nih.gov/gene/1288) · UniProt [Q14031](https://www.uniprot.org/uniprotkb/Q14031) · Ensembl [ENSG00000197565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197565)

## Data

Gene col 12419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12419); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12419]; `tensor/DDL_lfc|DDL_z.npy` [12419]; `embed/gene_vectors.npy` [12419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12419 or target_col == 12419). Every well: [[COL4A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
