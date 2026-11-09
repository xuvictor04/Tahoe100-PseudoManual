---
symbol: "CORIN"
type: "gene"
col: 6968
ensembl_id: "ENSG00000145244"
name: "corin, serine peptidase"
location: "4p12"
module: 37
arm: "+"
pooled_cpm: 15.24
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CORIN

*corin, serine peptidase* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +18.7, q 0e+00, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.320× (z -6.5, q 6e-08, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.78, fdr 7e-06), [[FRZB]] (+0.78, fdr 7e-06), [[SNX31]] (+0.76, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[TPTE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +18.7 | 0e+00 | 33/42 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +12.4 | 6e-33 | 32/41 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.98×** | +10.6 | 8e-24 | 30/41 (NCI-H23, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +9.6 | 7e-20 | 30/41 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.5 | 1e-08 | 22/42 (A498, SW 900, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **3.11×** | +6.4 | 1e-08 | 31/42 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 7e-07 | 19/42 (HOP62, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 25/41 (SW48, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 4e-05 | 20/41 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.5 | 4e-04 | 16/37 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.8 | 0.008 | 8/24 (LS 180, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Gefitinib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.036 | 10/43 (HT-29, LoVo, …) | top dose only |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.058 | 5/42 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.075 | 8/41 (NCI-H460, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.320×** | -6.5 | 6e-08 | 28/39 (SW 900, C32, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -5.6 | 7e-06 | 24/42 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.618×** | -5.0 | 9e-05 | 19/41 (A-427, SNU-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -4.3 | 0.002 | 20/41 (SNU-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -4.2 | 0.004 | 20/41 (KATO III, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.005 | 15/41 (CHP-212, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -3.5 | 0.044 | 17/41 (SW480, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.730×** | -3.2 | 0.086 | 11/41 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.732×** | -3.2 | 0.086 | 12/41 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 40.7 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0697× (z -19.7) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -16.2) |
| [[H4 (line)]] | wt | 58.9 | 0 | 6 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0885× (z -11.2) |
| [[KATO III (line)]] | alt | 56.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0361× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.152× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 101 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0977× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0289× (z -12.3) |
| [[SW480 (line)]] | alt | 11.7 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 72.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.9× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.0× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 11.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.2) | — |
| [[A-172 (line)]] | wt | 5.28 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +9.5) | [[5-Azacytidine (drug)]] 0.5 µM 0.0946× (z -8.6) |
| [[HOP62 (line)]] | alt | 8.39 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 14.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0371× (z -8.7) |
| [[A498 (line)]] | wt | 7.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0948× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.116× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0657× (z -8.9) |
| [[HT-29 (line)]] | alt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.93× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.197× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 4.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.93× (z +10.3) | — |
| [[SW 1271 (line)]] | alt | 72.0 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0644× (z -9.2) |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.78 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[FRZB]] | +0.78 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SNX31]] | +0.76 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[WDR49]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[MCF2]] | +0.75 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.75 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.74 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CASS4]] | +0.74 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.73 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[DRC1]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.73 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CORIN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CASC20]] | B | CASC20 activity raises CORIN's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.27× lower at baseline in the lines without CASC20 | 0.057 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises CORIN's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.05× lower at baseline in the lines without SLC26A4 | 0.090 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTE2]] | B | CORIN activity raises TPTE2's level | lines that do not express CORIN (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without CORIN | 0.060 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; its own permutation p |
| [[CCDC146]] | B | CORIN activity raises CCDC146's level | lines that do not express CORIN (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CORIN | 0.093 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent |
| [[TNFSF13B]] | B | CORIN activity raises TNFSF13B's level | lines that do not express CORIN (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CORIN | 0.099 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent |
| [[TNNI3K]] | C | CORIN activity raises TNNI3K's level | lines that do not express CORIN (5) vs lines expressing it (45) | 3.23× lower at baseline in the lines without CORIN | 0.060 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; co-absent with the target; its own permutation p |
| [[WDR49]] | C | CORIN activity raises WDR49's level | lines that do not express CORIN (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without CORIN | 0.092 | ⚠ within organs, on part of the lines; also absent: TNNI3K, WDR49, ENSG00000229195; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.1, -16.5); signed map (13.1, 5.5). **Vector** length 107, 25.8% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +18.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | corin, serine peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,593,999-47,838,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRSC, CRN, ATC2, Lrp4, TMPRSS10 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Reactome | 3 pathways, smallest: Physiological factors; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Q5](https://www.uniprot.org/uniprotkb/Q9Y5Q5) (Atrial natriuretic peptide-converting enzyme):

> Serine-type endopeptidase involved in atrial natriuretic peptide (NPPA) and brain natriuretic peptide (NPPB) processing. Converts through proteolytic cleavage the non-functional propeptides NPPA and NPPB into their active hormones, ANP and BNP(1-32) respectively, thereby regulating blood pressure in the heart and promoting natriuresis, diuresis and vasodilation. Proteolytic cleavage of pro-NPPA also plays a role in female pregnancy by promoting trophoblast invasion and spiral artery remodeling …

**Summary**, from NCBI Gene [10699](https://www.ncbi.nlm.nih.gov/gene/10699):

> This gene encodes a member of the type II transmembrane serine protease class of the trypsin superfamily. Members of this family are composed of multiple structurally distinct domains. The encoded protein converts pro-atrial natriuretic peptide to biologically active atrial natriuretic peptide, a cardiac hormone that regulates blood volume and pressure. This protein may also function as a pro-brain-type natriuretic peptide convertase. Multiple alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:19012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19012) · Entrez [10699](https://www.ncbi.nlm.nih.gov/gene/10699) · UniProt [Q9Y5Q5](https://www.uniprot.org/uniprotkb/Q9Y5Q5) · Ensembl [ENSG00000145244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145244)

## Data

Gene col 6968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6968); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6968]; `tensor/DDL_lfc|DDL_z.npy` [6968]; `embed/gene_vectors.npy` [6968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6968 or target_col == 6968). Every well: [[CORIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CORIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
