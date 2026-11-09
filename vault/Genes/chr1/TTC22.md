---
symbol: "TTC22"
type: "gene"
col: 116
ensembl_id: "ENSG00000006555"
name: "tetratricopeptide repeat domain 22"
location: "1p32.3"
module: 8
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 18
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 79
direction_downstream: 120
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TTC22

*tetratricopeptide repeat domain 22* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.56× (z +10.2, q 1e-21, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.05× (z +5.2, q 2e-05, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.505× (z -4.8, q 0.001, down in 15 of 16 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.0376×, LoVo 0.129×, CFPAC-1 0.137×, AsPC-1 0.0720×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.0361×, LS 180 0.0618×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.105×, CFPAC-1 0.174×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.244×, LoVo 0.268×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCNT3]] (+0.70, fdr 7e-06), [[CYP4F3]] (+0.67, fdr 1e-05), [[ABO]] (+0.67, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 79 arrows point to it, the strongest [[MSRB3]] → it (grade B ⚠); 120 go from it, the strongest it → [[KIAA1522]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.56×** | +10.2 | 1e-21 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.26×** | +10.1 | 1e-21 | 1/4 (LoVo) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.37×** | +6.3 | 6e-08 | 1/11 (NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.3 | 2e-05 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +5.2 | 2e-05 | 12/15 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.1 | 3e-05 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +5.0 | 5e-05 | 0/16 | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +4.9 | 8e-05 | 12/15 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.4 | 7e-04 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 0.002 | 11/15 (HT-29, COLO 205, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.22×** | +4.1 | 0.002 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.73×** | +4.0 | 0.004 | 1/15 (LoVo) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 0/14 | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.006 | 3/13 (Panc 03.27, KATO III, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.8 | 0.006 | 1/15 (KATO III) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +3.6 | 0.013 | 1/11 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.019 | 1/14 (HT-29) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.021 | 1/12 (SW1417) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.029 | 2/13 (KATO III, COLO 205) | inconsistent across doses | low cells (technical?) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.031 | 1/15 (COLO 205) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.047 | 1/15 (SW480) | top dose only | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.53×** | +3.0 | 0.051 | 0/15 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 116.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.0376×, LoVo 0.129×, CFPAC-1 0.137×, AsPC-1 0.0720×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.0361×, LS 180 0.0618×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.105×, CFPAC-1 0.174×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.244×, LoVo 0.268×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.505×** | -4.8 | 0.001 | 15/16 (NCI-H1573, COLO 205, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.547×** | -4.4 | 0.003 | 13/16 (LoVo, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.640× | -3.2 | 0.22 | 9/15 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.3) |
| [[SW1417 (line)]] | alt | 5.78 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0516× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.83 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0376× (z -18.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 5.60 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0361× (z -15.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 5.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.941 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT3]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CYP4F3]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[ABO]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[INAVA]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MUC4]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[C6orf132]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PROM1]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[USH1C]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TC2N]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[FUT2]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[ADCY4]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 5, C 74. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3]] | B | MSRB3 activity lowers TTC22's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.84× higher at baseline in the lines without MSRB3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises TTC22's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without RAPGEF5 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises TTC22's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without SLC44A3-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[IL22RA1]] | B | IL22RA1 activity raises TTC22's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without IL22RA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises TTC22's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without PLEKHG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[ITGB6]] | C | ITGB6 activity raises TTC22's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.16× lower at baseline in the lines without ITGB6 | 5e-05 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TTC22's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.40× lower at baseline in the lines without TMPRSS4 | 5e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises TTC22's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.20× lower at baseline in the lines without C1orf116 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[ST14]] | C | ST14 activity raises TTC22's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.17× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises TTC22's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.06× lower at baseline in the lines without CLIC5 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises TTC22's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.82× lower at baseline in the lines without ESRP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises TTC22's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.38× lower at baseline in the lines without INAVA | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |

### Downstream of this gene

*120 arrows, 120 of them with an alert ⚠; grade A 0, B 34, C 86. Shown: the 12 strongest; 108 more arrows (108 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | TTC22 activity raises KIAA1522's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without TTC22 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[DLG3]] | B | TTC22 activity raises DLG3's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.21× lower at baseline in the lines without TTC22 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[EPS8L1]] | B | TTC22 activity raises EPS8L1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.65× lower at baseline in the lines without TTC22 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[PLEKHA7]] | B | TTC22 activity raises PLEKHA7's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.20× lower at baseline in the lines without TTC22 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[IL22RA1]] | B | TTC22 activity raises IL22RA1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.24× lower at baseline in the lines without TTC22 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[TMEM62]] | B | TTC22 activity raises TMEM62's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.03× lower at baseline in the lines without TTC22 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[SLC44A3-AS1]] | B | TTC22 activity raises SLC44A3-AS1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.80× lower at baseline in the lines without TTC22 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[LMTK2]] | B | TTC22 activity raises LMTK2's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without TTC22 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[OCLN]] | B | TTC22 activity strengthens OCLN's drug response | lines that do not express TTC22 (15) vs lines expressing it (15) | the lines without TTC22 respond 0.23× as strongly (z diff +4.54); strongest at Homoharringtonine 5 µM: 1.03x vs 0.43x (z diff +7.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; target measured in part of the lines; artifact flags |
| [[FUT2]] | B | TTC22 activity raises FUT2's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without TTC22 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[ELMO3]] | B | TTC22 activity raises ELMO3's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.20× lower at baseline in the lines without TTC22 | 0.037 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[ARHGEF16]] | B | TTC22 activity raises ARHGEF16's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.86× lower at baseline in the lines without TTC22 | 0.044 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.9, 54.1); signed map (60.7, 5.1). **Vector** length 51.6, 16.3% of its response variance represented; |z| ≥ 3 in 389 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *O-linked glycosylation of mucins* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +4.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.3 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.3 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.2 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.8 | +0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,779,712-54,801,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20619 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q5TAA0](https://www.uniprot.org/uniprotkb/Q5TAA0) carries no function annotation.

**Summary**, from NCBI Gene [55001](https://www.ncbi.nlm.nih.gov/gene/55001):

> This gene encodes a protein with seven tetratricopeptide (TPR) repeats. Tetratricopeptide repeat containing motifs are found in a variety of proteins and may mediate protein-protein interactions and chaperone activity. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:26067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26067) · Entrez [55001](https://www.ncbi.nlm.nih.gov/gene/55001) · UniProt [Q5TAA0](https://www.uniprot.org/uniprotkb/Q5TAA0) · Ensembl [ENSG00000006555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006555)

## Data

Gene col 116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 116); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 116]; `tensor/DDL_lfc|DDL_z.npy` [116]; `embed/gene_vectors.npy` [116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 116 or target_col == 116). Every well: [[TTC22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
