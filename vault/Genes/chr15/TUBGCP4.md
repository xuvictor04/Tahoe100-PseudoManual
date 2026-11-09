---
symbol: "TUBGCP4"
type: "gene"
col: 6078
ensembl_id: "ENSG00000137822"
name: "tubulin gamma complex component 4"
location: "15q15.3"
module: 18
arm: "+"
pooled_cpm: 25.48
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TUBGCP4

*tubulin gamma complex component 4* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.49× (z +8.8, q 6e-16, up in 36 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 1.21× (z +4.2, q 0.001, up in 18 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.175×, SW48 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.457×, RKO 0.469×; ⚠ cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.102×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.333×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1E1]] (+0.76, fdr 7e-06), [[CAD]] (+0.74, fdr 7e-06), [[ADAT2]] (+0.74, fdr 7e-06); moves opposite to [[WBP1]] (-0.63, fdr 7e-06), [[SELENOK]] (-0.61, fdr 1e-05), [[GOLGB1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +8.8 | 6e-16 | 36/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.38×** | +6.8 | 3e-09 | 19/36 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +6.6 | 9e-09 | 24/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.34×** | +6.3 | 6e-08 | 24/46 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.32×** | +6.2 | 8e-08 | 23/44 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +5.7 | 1e-06 | 22/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.27×** | +5.3 | 1e-05 | 20/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +5.2 | 1e-05 | 17/48 (AsPC-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.18× | +5.2 | 2e-05 | 16/48 (NCI-H1792, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +5.0 | 4e-05 | 19/47 (NCI-H23, SHP-77, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.24×** | +4.6 | 2e-04 | 19/47 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +4.3 | 7e-04 | 17/48 (LoVo, SHP-77, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.22×** | +4.3 | 9e-04 | 14/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +4.2 | 0.001 | 18/47 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 7/48 (NCI-H460, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.005 | 11/47 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.017 | 6/46 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.025 | 5/48 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.029 | 10/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.042 | 5/47 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +2.9 | 0.080 | 8/48 (SW 900, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.175×, SW48 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.457×, RKO 0.469×; ⚠ cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.102×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.333×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.848× | -5.2 | 1e-04 | 21/47 (LoVo, RKO, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.2 | 0.007 | 3/48 (SW 900, NCI-H661, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.851× | -3.6 | 0.060 | 13/47 (A-427, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.763× | -3.1 | 0.23 | 6/48 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -11.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.102× (z -8.9) |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.333× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 28.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.34× (z +9.2) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1E1]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[CAD]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[CDCA7]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MDN1]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[SORD]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[RPE]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[URB2]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ANAPC1]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[XYLB]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[GMPS]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1]] | -0.63 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[MXD1]] | -0.59 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[COQ10B]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CWC25]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CCDC186]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises TUBGCP4's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without TSEN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.1, -37.3); signed map (-4.3, -51.9). **Vector** length 82.6, 15.6% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +5.9 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.8 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +3.6 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.9 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma complex component 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,369,221-43,409,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 76P, FLJ14797, GCP4 |
| Gene groups (HGNC) | Tubulin gamma complex component family |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGJ1](https://www.uniprot.org/uniprotkb/Q9UGJ1) (Gamma-tubulin complex component 4):

> Component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [27229](https://www.ncbi.nlm.nih.gov/gene/27229):

> This gene encodes a component of the gamma-tubulin ring complex, which is required for microtubule nucleation. In mammalian cells, the protein localizes to centrosomes in association with gamma-tubulin. Crystal structure analysis revealed a structure composed of five helical bundles arranged around conserved hydrophobic cores. An exposed surface area located in the C-terminal domain is essential and sufficient for direct binding to gamma-tubulin. Mutations in this gene that alter microtubule …

**Accessions** — [HGNC:16691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16691) · Entrez [27229](https://www.ncbi.nlm.nih.gov/gene/27229) · UniProt [Q9UGJ1](https://www.uniprot.org/uniprotkb/Q9UGJ1) · Ensembl [ENSG00000137822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137822)

## Data

Gene col 6078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6078); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6078]; `tensor/DDL_lfc|DDL_z.npy` [6078]; `embed/gene_vectors.npy` [6078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6078 or target_col == 6078). Every well: [[TUBGCP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBGCP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
