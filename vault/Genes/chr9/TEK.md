---
symbol: "TEK"
type: "gene"
col: 4162
ensembl_id: "ENSG00000120156"
name: "TEK receptor tyrosine kinase"
location: "9p21.2"
module: 13
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 23
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TEK

*TEK receptor tyrosine kinase* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.95× (z +20.7, q 0e+00, up in 6 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 0.0880×, Hs 766T 0.156×, hTERT-HPNE 0.101×); [[Belinostat (drug)]] 5 µM in 2 lines (A-172 0.0120×, Hs 766T 0.103×; ⚠ cell-cycle shift, explains ~47% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.0775×, A-172 0.0955×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0570×, Hs 766T 0.123×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.0775×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIRAS3]] (+0.60, fdr 1e-05), [[IPO9-AS1]] (+0.58, fdr 1e-05), [[LMO2]] (+0.58, fdr 2e-05); moves opposite to [[DTNB]] (-0.43, fdr 1e-04), [[PTGES2]] (-0.39, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[DDR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.95×** | +20.7 | 0e+00 | 6/9 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.81×** | +18.2 | 0e+00 | 7/10 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +10.8 | 5e-25 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +10.7 | 9e-25 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.38×** | +10.0 | 2e-21 | 3/10 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.30×** | +9.4 | 4e-19 | 7/13 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +8.0 | 1e-13 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +7.1 | 1e-10 | 7/14 (SK-MEL-2, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.4 | 5e-06 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.7 | 2e-04 | 3/16 (LOX-IMVI, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 2/12 (LOX-IMVI, LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 1/16 (HEC-1-A) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +4.2 | 0.001 | 1/7 (A498) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.1 | 0.002 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.9 | 0.004 | 0/7 | top dose only |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.025 | 0/8 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.042 | 4/16 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.042 | 0/8 | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.047 | 3/15 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.047 | 1/9 (HEC-1-A) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4162.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 0.0880×, Hs 766T 0.156×, hTERT-HPNE 0.101×); [[Belinostat (drug)]] 5 µM in 2 lines (A-172 0.0120×, Hs 766T 0.103×; ⚠ cell-cycle shift, explains ~47% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.0775×, A-172 0.0955×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0570×, Hs 766T 0.123×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.0775×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.631× | -3.2 | 0.59 | 3/17 (HCT15, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 97.1 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -19.4) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0120× (z -19.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0584× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0570× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 0.965 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.4× (z +9.8) | — |
| [[A-427 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.555 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIRAS3]] | +0.60 | +0.70 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[IPO9-AS1]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LMO2]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[DENND2A]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PAMR1]] | +0.57 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[MXRA5]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[KIAA1614]] | +0.56 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[SUCNR1]] | +0.55 | +0.65 / +0.43 | both halves | 3e-05 | **novel candidate** |
| [[B3GNT9]] | +0.55 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[LINC01615]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LRRC17]] | +0.54 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[COL5A1]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNB]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[PTGES2]] | -0.39 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BAALC]] | C | BAALC activity raises TEK's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.20× lower at baseline in the lines without BAALC | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises TEK's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without LINC01592 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[SULF1]] | C | SULF1 activity raises TEK's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.82× lower at baseline in the lines without SULF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises TEK's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without PTGFR | 0.048 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises TEK's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without ADAMTS6 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[ARHGEF6]] | C | ARHGEF6 activity raises TEK's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without ARHGEF6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises TEK's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.70× lower at baseline in the lines without SEMA5A | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDR2]] | B | TEK activity raises DDR2's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without TEK | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent |
| [[CFAP20DC-DT]] | B | TEK activity raises CFAP20DC-DT's level | lines that do not express TEK (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without TEK | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent |
| [[NMNAT2]] | B | TEK activity raises NMNAT2's level | lines that do not express TEK (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without TEK | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent |
| [[DKK3]] | C | TEK activity raises DKK3's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without TEK | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[SULF1]] | C | TEK activity raises SULF1's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without TEK | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | TEK activity raises SEMA5A's level | lines that do not express TEK (27) vs lines expressing it (23) | 3.70× lower at baseline in the lines without TEK | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[ABI3BP]] | C | TEK activity raises ABI3BP's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without TEK | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[COL5A1]] | C | TEK activity raises COL5A1's level | lines that do not express TEK (27) vs lines expressing it (23) | 3.25× lower at baseline in the lines without TEK | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[ADAMTS6]] | C | TEK activity raises ADAMTS6's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without TEK | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[ADAMTS2]] | C | TEK activity raises ADAMTS2's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.77× lower at baseline in the lines without TEK | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[JAM2]] | C | TEK activity raises JAM2's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without TEK | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[ITGA8]] | C | TEK activity raises ITGA8's level | lines that do not express TEK (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without TEK | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (57.1, 19.3); signed map (27.7, 51.5). **Vector** length 38.3, 8.94% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +18.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +20.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TEK receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:27,109,141-27,230,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIE2, TIE-2, VMCM1, CD202b; previously VMCM |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Immunoglobulin like domain containing; Tyrosine kinase with immunoglobulin like and EGF like domains family |
| Reactome | 6 pathways, smallest: Tie2 Signaling; Cell surface interactions at the vascular wall; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02763](https://www.uniprot.org/uniprotkb/Q02763) (Angiopoietin-1 receptor):

> Tyrosine-protein kinase that acts as a cell-surface receptor for ANGPT1, ANGPT2 and ANGPT4 and regulates angiogenesis, endothelial cell survival, proliferation, migration, adhesion and cell spreading, reorganization of the actin cytoskeleton, but also maintenance of vascular quiescence. Has anti-inflammatory effects by preventing the leakage of pro-inflammatory plasma proteins and leukocytes from blood vessels. Required for normal angiogenesis and heart development during embryogenesis. …

**Summary**, from NCBI Gene [7010](https://www.ncbi.nlm.nih.gov/gene/7010):

> This gene encodes a receptor that belongs to the protein tyrosine kinase Tie2 family. The encoded protein possesses a unique extracellular region that contains two immunoglobulin-like domains, three epidermal growth factor (EGF)-like domains and three fibronectin type III repeats. The ligand angiopoietin-1 binds to this receptor and mediates a signaling pathway that functions in embryonic vascular development. Mutations in this gene are associated with inherited venous malformations of the skin …

**Accessions** — [HGNC:11724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11724) · Entrez [7010](https://www.ncbi.nlm.nih.gov/gene/7010) · UniProt [Q02763](https://www.uniprot.org/uniprotkb/Q02763) · Ensembl [ENSG00000120156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120156)

## Data

Gene col 4162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4162); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4162]; `tensor/DDL_lfc|DDL_z.npy` [4162]; `embed/gene_vectors.npy` [4162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4162 or target_col == 4162). Every well: [[TEK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
