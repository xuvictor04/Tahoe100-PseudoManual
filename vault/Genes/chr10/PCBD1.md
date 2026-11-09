---
symbol: "PCBD1"
type: "gene"
col: 9266
ensembl_id: "ENSG00000166228"
name: "pterin-4 alpha-carbinolamine dehydratase 1"
location: "10q22.1"
module: 60
arm: "+"
pooled_cpm: 19.32
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PCBD1

*pterin-4 alpha-carbinolamine dehydratase 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.13× (z +10.3, q 4e-22, up in 34 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.89× (z +4.6, q 5e-04, up in 30 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 6.51×, A498 4.18×, KATO III 5.08×, SW480 4.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 6.24×, NCI-H460 5.15×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.363× (z -10.2, q 7e-22, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.67, fdr 7e-06), [[HSP90AB2P]] (+0.61, fdr 1e-05), [[CLPP]] (+0.60, fdr 1e-05); moves opposite to [[BCL9L]] (-0.52, fdr 4e-05), [[PLEC]] (-0.50, fdr 1e-04), [[METTL25B]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CMTM8]] → it (grade B ⚠); 2 go from it, the strongest it → [[CMTM8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9266.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 6.51×, A498 4.18×, KATO III 5.08×, SW480 4.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 6.24×, NCI-H460 5.15×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.13×** | +10.3 | 4e-22 | 34/36 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +8.8 | 4e-16 | 27/28 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +4.9 | 2e-04 | 25/30 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +4.6 | 5e-04 | 30/44 (KATO III, J82, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.73×** | +4.0 | 0.007 | 23/40 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.363×** | -10.2 | 7e-22 | 38/44 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.376×** | -7.1 | 4e-10 | 37/43 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.391×** | -6.8 | 2e-09 | 35/44 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -5.0 | 1e-04 | 31/44 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -4.1 | 0.006 | 27/44 (AN3 CA, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.641× | -3.2 | 0.13 | 19/44 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.639× | -3.1 | 0.15 | 24/43 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.398× | -3.0 | 0.18 | 25/43 (LS 180, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.9) |
| [[LoVo (line)]] | wt | 25.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0648× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.8) |
| [[RKO (line)]] | wt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.4) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -16.6) |
| [[SW480 (line)]] | alt | 30.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.5) |
| [[A498 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.6) |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -8.9) |
| [[HS-578T (line)]] | alt | 7.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -12.6) |
| [[HT-29 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.282× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0808× (z -15.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.9) |
| [[PANC-1 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 6.07 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.05 µM 0.0602× (z -9.3) |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.9) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HSP90AB2P]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CLPP]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PTRHD1]] ⚠ | +0.59 | +0.49 / +0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SPR]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 | STRING 852 |
| [[PSMA1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[ATP2C1]] | +0.58 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[HIBCH]] | +0.58 | +0.57 / +0.40 | both halves | 4e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[HSP90AB3P]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CACYBP]] | +0.57 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[SLC25A26]] | +0.57 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[UBE4B]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[HSPE1]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL9L]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PLEC]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[METTL25B]] | -0.49 | -0.63 / -0.28 | both halves | 3e-04 |  |
| [[PLXNB2]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MDC1]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PAN2]] | -0.47 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM8]] | B | CMTM8 activity raises PCBD1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without CMTM8 | 0.023 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PCBD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00839]] | B | LINC00839 activity lowers PCBD1's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 1.97× higher at baseline in the lines without LINC00839 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10 |
| [[EGFL7]] | B | EGFL7 activity raises PCBD1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without EGFL7 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[FAM241B]] | C | FAM241B activity raises PCBD1's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent; its own permutation p |
| [[PLEC]] | C | PLEC activity raises PCBD1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.30× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM8]] | C | PCBD1 activity raises CMTM8's level | lines that do not express PCBD1 (3) vs lines expressing it (47) | 4.89× lower at baseline in the lines without PCBD1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FZD5, EZR, ZBED3; maybe low, not absent; its own permutation p |
| [[CHCHD10]] | C | PCBD1 activity raises CHCHD10's level | lines that do not express PCBD1 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without PCBD1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FZD5, EZR, ZBED3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.8, -12.1); signed map (-29.3, -24.7). **Vector** length 50.3, 11.4% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | pterin-4 alpha-carbinolamine dehydratase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,882,280-70,888,565 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCD; previously DCOH, PCBD |
| Gene groups (HGNC) | Pterin-4 alpha-carbinolamine dehydratases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Phenylalanine metabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P61457](https://www.uniprot.org/uniprotkb/P61457) (Pterin-4-alpha-carbinolamine dehydratase):

> Involved in tetrahydrobiopterin biosynthesis (By similarity). Seems to both prevent the formation of 7-pterins and accelerate the formation of quinonoid-BH2. Coactivator for HNF1A-dependent transcription (By similarity). Regulates the dimerization of homeodomain protein HNF1A and enhances its transcriptional activity (By similarity). Also acts as a coactivator for HNF1B-dependent transcription.

**Summary**, from NCBI Gene [5092](https://www.ncbi.nlm.nih.gov/gene/5092):

> This gene encodes a member of the pterin-4-alpha-carbinolamine dehydratase family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. The encoded protein functions as both a dehydratase involved in tetrahydrobiopterin biosynthesis, and as a cofactor for HNF1A-dependent transcription. A deficiency of this enzyme leads to hyperphenylalaninemia. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:8646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8646) · Entrez [5092](https://www.ncbi.nlm.nih.gov/gene/5092) · UniProt [P61457](https://www.uniprot.org/uniprotkb/P61457) · Ensembl [ENSG00000166228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166228)

## Data

Gene col 9266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9266); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9266]; `tensor/DDL_lfc|DDL_z.npy` [9266]; `embed/gene_vectors.npy` [9266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9266 or target_col == 9266). Every well: [[PCBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
