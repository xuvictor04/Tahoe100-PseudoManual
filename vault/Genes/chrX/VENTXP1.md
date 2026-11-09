---
symbol: "VENTXP1"
type: "gene"
col: 15239
ensembl_id: "ENSG00000259849"
name: "VENT homeobox pseudogene 1"
location: "Xp21.3"
module: 90
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 38
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 8
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# VENTXP1

*VENT homeobox pseudogene 1* — Xp21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.33× (z +13.3, q 2e-37, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.29× (z +12.6, q 9e-34, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Benproperine (phosphate) (drug)]] 0.05 µM: 0.574× (z -3.9, q 0.054, down in 3 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.248×); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.200×; ⚠ cell-cycle shift, explains ~22% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.211×; ⚠ cell-cycle shift, explains ~65% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYT1L]] (+0.83, fdr 7e-06), [[LINC02306]] (+0.78, fdr 7e-06), [[CNTNAP5]] (+0.75, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 8 go from it, the strongest it → [[ENTPD5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.33×** | +13.3 | 2e-37 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +12.6 | 9e-34 | 12/17 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +10.6 | 9e-24 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +10.1 | 5e-22 | 10/19 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.04×** | +9.7 | 5e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +8.5 | 2e-15 | 15/21 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.91×** | +4.8 | 1e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +4.6 | 3e-04 | 6/27 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +4.1 | 0.003 | 5/26 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +3.9 | 0.005 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +3.9 | 0.005 | 1/1 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.012 | 1/29 (SHP-77) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +3.6 | 0.017 | 7/17 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.5 | 0.017 | 1/3 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.4 | 0.022 | 0/6 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.035 | 1/11 (SHP-77) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.1 | 0.053 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.053 | 1/8 (NCI-H460) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.055 | 0/8 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.248×); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.200×; ⚠ cell-cycle shift, explains ~22% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.211×; ⚠ cell-cycle shift, explains ~65% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.574×** | -3.9 | 0.054 | 3/26 (Panc 03.27, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 141 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.74× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -14.2) |
| [[A-172 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.926 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYT1L]] | +0.83 | +0.80 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC02306]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.75 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[GLRA3]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[RALYL]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.73 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CHRM5]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.71 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises VENTXP1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.20× lower at baseline in the lines without CALCA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[LINC01320]] | B | LINC01320 activity raises VENTXP1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.56× lower at baseline in the lines without LINC01320 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[RIT2]] | B | RIT2 activity raises VENTXP1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.38× lower at baseline in the lines without RIT2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[SRRM4]] | B | SRRM4 activity raises VENTXP1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without SRRM4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[SYT4]] | B | SYT4 activity raises VENTXP1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.32× lower at baseline in the lines without SYT4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[ASCL1]] | B | ASCL1 activity raises VENTXP1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.74× lower at baseline in the lines without ASCL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[PDZRN3]] | B | PDZRN3 activity raises VENTXP1's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without PDZRN3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[KCNB2]] | B | KCNB2 activity raises VENTXP1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.85× lower at baseline in the lines without KCNB2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[LINC02492]] | B | LINC02492 activity raises VENTXP1's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without LINC02492 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[CGA]] | B | CGA activity raises VENTXP1's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.25× lower at baseline in the lines without CGA | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[BAALC]] | B | BAALC activity raises VENTXP1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without BAALC | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[F11-AS1]] | B | F11-AS1 activity weakens VENTXP1's drug response | lines that do not express F11-AS1 (23) vs lines expressing it (6) | the lines without F11-AS1 respond 4.88× as strongly (z diff -1.17); strongest at Dinaciclib 0.5 µM: 6.17x vs 0.39x (z diff -11.4) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTPD5]] | B | VENTXP1 activity lowers ENTPD5's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.37× higher at baseline in the lines without VENTXP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[OBI1-AS1]] | B | VENTXP1 activity raises OBI1-AS1's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without VENTXP1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 0.5 µM | B | VENTXP1 activity raises the cells' numbers under Docetaxel 0.5 µM (protects the cells) | lines that do not express VENTXP1 (12) vs lines expressing it (36) | the lines without VENTXP1: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[MYO16]] | B | VENTXP1 activity raises MYO16's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without VENTXP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 5 µM | B | VENTXP1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express VENTXP1 (12) vs lines expressing it (36) | the lines without VENTXP1: 0.89× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[CHRM5]] | C | VENTXP1's natural level weakens CHRM5's drug response | VENTXP1's natural level across 32 lines (lineage-adjusted; a glimpse) | r -0.84, reverse -0.54; direction clear | 0.019 | ⚠ tissue can mimic it; precision caveat |
| [[CLVS1]] | C | VENTXP1's natural level weakens CLVS1's drug response | VENTXP1's natural level across 33 lines (lineage-adjusted; a glimpse) | r -0.82, reverse -0.61; direction not clear | 0.020 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PTPRT]] | C | VENTXP1's natural level weakens PTPRT's drug response | VENTXP1's natural level across 32 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.40; direction clear | 0.075 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.4, 30.0); signed map (34.6, 15.7). **Vector** length 28.8, 3.73% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | VENT homeobox pseudogene 1 |
| Locus type | pseudogene |
| Location | Xp21.3 — chrX:26,557,675-26,558,330 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | NA88A, CT18 |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Matched by | ensembl_id |

UniProt [P0C5K6](https://www.uniprot.org/uniprotkb/P0C5K6) carries no function annotation.

**Summary**, from NCBI Gene [139538](https://www.ncbi.nlm.nih.gov/gene/139538):

> Homeobox genes encode DNA-binding proteins, many of which are thought to be involved in early embryonic development. Homeobox genes encode a DNA-binding domain of 60 to 63 amino acids referred to as the homeodomain. This pseudogene is a member of the Vent homeobox gene family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30900) · Entrez [139538](https://www.ncbi.nlm.nih.gov/gene/139538) · UniProt [P0C5K6](https://www.uniprot.org/uniprotkb/P0C5K6) · Ensembl [ENSG00000259849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259849)

## Data

Gene col 15239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15239); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15239]; `tensor/DDL_lfc|DDL_z.npy` [15239]; `embed/gene_vectors.npy` [15239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15239 or target_col == 15239). Every well: [[VENTXP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VENTXP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
