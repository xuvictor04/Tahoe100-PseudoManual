---
symbol: "ADAMTSL3"
type: "gene"
col: 7958
ensembl_id: "ENSG00000156218"
name: "ADAMTS like 3"
location: "15q25.2"
module: 9
arm: "+"
pooled_cpm: 8.64
n_lines_expressing: 21
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADAMTSL3

*ADAMTS like 3* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +18.4, q 0e+00, up in 4 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Dihydroartemisinin (drug)]] 0.5 µM: 0.712× (z -3.8, q 0.072, down in 4 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.246×, NCI-H2030 0.302×, NCI-H1573 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (Hs 766T 0.0420×, NCI-H2030 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0424×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.133×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-423 0.101×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.423×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALCRL]] (+0.54, fdr 1e-05), [[ECSCR]] (+0.53, fdr 3e-05), [[SNTG2]] (+0.51, fdr 2e-04); moves opposite to [[ASTE1]] (-0.46, fdr 1e-04), [[LSM14B]] (-0.44, fdr 6e-05), [[GEMIN8]] (-0.44, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CNTNAP3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +18.4 | 0e+00 | 4/16 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +12.5 | 2e-33 | 3/8 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.5 | 3e-33 | 6/13 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +11.5 | 2e-28 | 13/19 (BT-474, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +11.1 | 9e-27 | 3/9 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +7.8 | 5e-13 | 10/17 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +5.8 | 5e-07 | 3/18 (A549, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 4/19 (A-172, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.8 | 1e-04 | 0/13 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.8 | 1e-04 | 1/13 (A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 5/17 (A-172, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +4.4 | 6e-04 | 1/9 (NCI-H1573) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.3 | 6e-04 | 1/14 (A549) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 2/16 (BT-474, A549) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.011 | 9/19 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.011 | 9/18 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.020 | 4/19 (NCI-H1573, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7958.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.246×, NCI-H2030 0.302×, NCI-H1573 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (Hs 766T 0.0420×, NCI-H2030 0.237×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0424×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.133×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-423 0.101×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.423×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.712×** | -3.8 | 0.072 | 4/18 (A-172, A549, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.090 | 0/19 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.748× | -3.3 | 0.15 | 7/16 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.748× | -3.3 | 0.15 | 0/18 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.766× | -3.0 | 0.29 | 1/19 (H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 67.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.7) |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0424× (z -14.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0420× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[SNU-423 (line)]] | alt | 7.18 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[A-172 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCRL]] | +0.54 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ECSCR]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SNTG2]] | +0.51 | +0.29 / +0.62 | both halves | 2e-04 |  |
| [[HBG2]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[SLC6A17]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[DSCAM]] | +0.50 | +0.44 / +0.55 | both halves | 3e-05 | same gene group |
| [[ANOS1]] | +0.50 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[KISS1]] | +0.50 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[SCEL]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[NEGR1]] | +0.49 | +0.33 / +0.55 | both halves | 1e-04 | same gene group |
| [[AKAP6]] | +0.49 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[FMN2]] | +0.49 | +0.46 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASTE1]] | -0.46 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[LSM14B]] | -0.44 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[GEMIN8]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[EMC2]] | -0.44 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[HPS4]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[COQ9]] | -0.42 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[TM2D3]] | -0.41 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[TTC21A]] | -0.41 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[YJU2B]] | -0.41 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[PEX11B]] | -0.41 | -0.30 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAMTSL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02484]] | C | LINC02484 activity raises ADAMTSL3's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 3.18× lower at baseline in the lines without LINC02484 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3C]] | B | ADAMTSL3 activity raises CNTNAP3C's level | lines that do not express ADAMTSL3 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without ADAMTSL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ANOS1, NTRK3, PSG4; maybe low, not absent |
| [[LINC02725]] | B | ADAMTSL3 activity raises LINC02725's level | lines that do not express ADAMTSL3 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without ADAMTSL3 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANOS1, NTRK3, PSG4; maybe low, not absent |
| [[CNTNAP3]] | C | ADAMTSL3 activity raises CNTNAP3's level | lines that do not express ADAMTSL3 (29) vs lines expressing it (21) | 2.75× lower at baseline in the lines without ADAMTSL3 | 0.017 | ⚠ within organs, on part of the lines; also absent: ANOS1, NTRK3, PSG4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.6, 19.2); signed map (34.2, 30.3). **Vector** length 38.3, 7.66% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTS like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:83,654,088-84,039,842 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1233, punctin-2 |
| Gene groups (HGNC) | I-set domain containing; Immunoglobulin like domain containing; ADAMTS like |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [P82987](https://www.uniprot.org/uniprotkb/P82987) carries no function annotation.

**Summary**, from NCBI Gene [57188](https://www.ncbi.nlm.nih.gov/gene/57188):

> Predicted to be involved in extracellular matrix organization. Predicted to be active in extracellular matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14633) · Entrez [57188](https://www.ncbi.nlm.nih.gov/gene/57188) · UniProt [P82987](https://www.uniprot.org/uniprotkb/P82987) · Ensembl [ENSG00000156218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156218)

## Data

Gene col 7958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7958); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7958]; `tensor/DDL_lfc|DDL_z.npy` [7958]; `embed/gene_vectors.npy` [7958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7958 or target_col == 7958). Every well: [[ADAMTSL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTSL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
