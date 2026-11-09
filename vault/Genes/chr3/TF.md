---
symbol: "TF"
type: "gene"
col: 1666
ensembl_id: "ENSG00000091513"
name: "transferrin"
location: "3q22.1"
module: 87
arm: "+"
pooled_cpm: 13.38
n_lines_expressing: 9
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 21
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TF

*transferrin* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.23× (z +16.6, q 0e+00, up in 3 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.214×; ⚠ cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.145×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A2M]] (+0.86, fdr 7e-06), [[LHFPL3-AS1]] (+0.83, fdr 7e-06), [[TYR]] (+0.80, fdr 7e-06); moves opposite to [[PYDC2-AS1]] (-0.45, fdr 2e-04), [[EML6]] (-0.38, fdr 3e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 21 go from it, the strongest it → [[FAXDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.23×** | +16.6 | 0e+00 | 3/6 (HepG2/C3A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.58×** | +12.2 | 1e-31 | 1/3 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +11.0 | 8e-26 | 2/2 (HepG2/C3A, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +9.9 | 5e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +6.6 | 4e-09 | 1/4 (C-33 A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +6.2 | 7e-08 | 0/5 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.7 | 8e-07 | 1/4 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.1 | 2e-05 | 1/7 (C-33 A) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +4.9 | 6e-05 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +4.8 | 8e-05 | 0/4 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.36×** | +4.3 | 7e-04 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.52×** | +4.2 | 0.001 | 0/4 | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +4.1 | 0.001 | 1/2 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.006 | 2/5 (HepG2/C3A, SK-MEL-2) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.56×** | +3.1 | 0.065 | 2/5 (C32, RPMI-7951) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1666.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.214×; ⚠ cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.145×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.634× | -3.3 | 0.61 | 3/6 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.742× | -3.0 | 0.62 | 0/7 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 971 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -12.6) |
| [[A-172 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A2M]] | +0.86 | +0.90 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 820 |
| [[LHFPL3-AS1]] | +0.83 | +0.85 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TYR]] | +0.80 | +0.84 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[APOD]] | +0.73 | +0.73 / +0.49 | both halves | 1e-05 | STRING 428 |
| [[FCRLA]] | +0.69 | +0.77 / +0.40 | both halves | 4e-05 | **novel candidate** |
| [[LINC02941]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SOX10]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PI15]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RMEL3]] | +0.63 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[TET1]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CTTNBP2]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CFI]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYDC2-AS1]] | -0.45 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[EML6]] | -0.38 | -0.45 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RHOJ]] | C | RHOJ activity raises TF's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without RHOJ | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[TYR]] | C | TYR activity raises TF's level | lines that do not express TYR (43) vs lines expressing it (7) | 2.96× lower at baseline in the lines without TYR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises TF's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 3.17× lower at baseline in the lines without LHFPL3-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises TF's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without AEBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises TF's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.61× lower at baseline in the lines without COL19A1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[PEG3]] | C | PEG3 activity raises TF's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.17× lower at baseline in the lines without PEG3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[A2M]] | C | A2M activity raises TF's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.96× lower at baseline in the lines without A2M | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[SOX10]] | C | SOX10 activity raises TF's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 3.70× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[APOD]] | C | APOD activity raises TF's level | lines that do not express APOD (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without APOD | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises TF's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without LOXL3 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[MGP]] | C | MGP activity raises TF's level | lines that do not express MGP (35) vs lines expressing it (15) | 1.44× lower at baseline in the lines without MGP | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 2, C 19. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXDC2]] | B | TF activity raises FAXDC2's level | lines that do not express TF (41) vs lines expressing it (9) | 2.26× lower at baseline in the lines without TF | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1 |
| [[CFAP20DC-DT]] | B | TF activity raises CFAP20DC-DT's level | lines that do not express TF (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without TF | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1 |
| [[A2M]] | C | TF activity raises A2M's level | lines that do not express TF (41) vs lines expressing it (9) | 12.32× lower at baseline in the lines without TF | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[AEBP1]] | C | TF activity raises AEBP1's level | lines that do not express TF (41) vs lines expressing it (9) | 5.21× lower at baseline in the lines without TF | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[LHFPL3-AS1]] | C | TF activity raises LHFPL3-AS1's level | lines that do not express TF (41) vs lines expressing it (9) | 7.11× lower at baseline in the lines without TF | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[LOXL3]] | C | TF activity raises LOXL3's level | lines that do not express TF (41) vs lines expressing it (9) | 4.03× lower at baseline in the lines without TF | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[MIR3681HG]] | C | TF activity raises MIR3681HG's level | lines that do not express TF (41) vs lines expressing it (9) | 7.47× lower at baseline in the lines without TF | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[FCRLA]] | C | TF activity raises FCRLA's level | lines that do not express TF (41) vs lines expressing it (9) | 4.26× lower at baseline in the lines without TF | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[TIMP3]] | C | TF activity raises TIMP3's level | lines that do not express TF (41) vs lines expressing it (9) | 6.83× lower at baseline in the lines without TF | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[SOX10]] | C | TF activity raises SOX10's level | lines that do not express TF (41) vs lines expressing it (9) | 5.41× lower at baseline in the lines without TF | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[GPNMB]] | C | TF activity raises GPNMB's level | lines that do not express TF (41) vs lines expressing it (9) | 6.79× lower at baseline in the lines without TF | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[DAAM2]] | C | TF activity raises DAAM2's level | lines that do not express TF (41) vs lines expressing it (9) | 3.78× lower at baseline in the lines without TF | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.7, 29.1); signed map (29.9, 39.9). **Vector** length 21.1, 7.17% of its response variance represented; |z| ≥ 3 in 156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +16.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +0.7 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.7 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.5 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +1.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.5 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.5 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transferrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,746,040-133,796,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1557, PRO2086 |
| Gene groups (HGNC) | Transferrins |
| Hallmark sets | COAGULATION |
| Reactome | 13 pathways, smallest: Transferrin endocytosis and recycling; Iron uptake and transport; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P02787](https://www.uniprot.org/uniprotkb/P02787) (Serotransferrin):

> Transferrins are iron binding transport proteins which can bind two Fe(3+) ions in association with the binding of an anion, usually bicarbonate. It is responsible for the transport of iron from sites of absorption and heme degradation to those of storage and utilization. Serum transferrin may also have a further role in stimulating cell proliferation.; (Microbial infection) Serves as an iron source for Neisseria species, which capture the protein and extract its iron for their own use.; …

**Summary**, from NCBI Gene [7018](https://www.ncbi.nlm.nih.gov/gene/7018):

> This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells to all proliferating cells in the body. This protein may also have a physiologic role as …

**Accessions** — [HGNC:11740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11740) · Entrez [7018](https://www.ncbi.nlm.nih.gov/gene/7018) · UniProt [P02787](https://www.uniprot.org/uniprotkb/P02787) · Ensembl [ENSG00000091513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091513)

## Data

Gene col 1666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1666); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1666]; `tensor/DDL_lfc|DDL_z.npy` [1666]; `embed/gene_vectors.npy` [1666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1666 or target_col == 1666). Every well: [[TF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
