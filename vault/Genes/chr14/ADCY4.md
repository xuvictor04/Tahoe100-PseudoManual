---
symbol: "ADCY4"
type: "gene"
col: 4974
ensembl_id: "ENSG00000129467"
name: "adenylate cyclase 4"
location: "14q12"
module: 8
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 17
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 118
direction_downstream: 132
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ADCY4

*adenylate cyclase 4* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.30× (z +10.3, q 5e-22, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +8.2, q 5e-14, up in 1 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.569× (z -3.6, q 0.063, down in 14 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 0.0968×, HT-29 0.133×, SW480 0.153×, NCI-H1573 0.171×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.161×, COLO 205 0.252×, CFPAC-1 0.287×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 0.0362×, SW480 0.0682×, Panc 03.27 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMC4]] (+0.78, fdr 7e-06), [[TMEM45B]] (+0.74, fdr 7e-06), [[TMEM125]] (+0.74, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 118 arrows point to it, the strongest [[DCLK2]] → it (grade B ⚠); 132 go from it, the strongest it → [[SDCBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.30×** | +10.3 | 5e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +9.1 | 4e-17 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +8.9 | 1e-16 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +8.2 | 5e-14 | 1/13 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.2 | 3e-05 | 2/10 (LS 180, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.73×** | +4.6 | 4e-04 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.001 | 1/13 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.1 | 0.003 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.8 | 0.009 | 5/12 (AsPC-1, SW480, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.019 | 1/13 (SW480) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.5 | 0.023 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.5 | 0.023 | 2/11 (SW480, CFPAC-1) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.023 | 7/15 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.038 | 7/14 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +3.2 | 0.046 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.095 | 5/13 (SW480, Panc 03.27, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 0.0968×, HT-29 0.133×, SW480 0.153×, NCI-H1573 0.171×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.161×, COLO 205 0.252×, CFPAC-1 0.287×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 0.0362×, SW480 0.0682×, Panc 03.27 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -3.6 | 0.063 | 14/15 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.676×** | -3.6 | 0.063 | 5/15 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -3.6 | 0.063 | 12/15 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.603× | -3.3 | 0.15 | 9/15 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.600× | -3.1 | 0.25 | 4/15 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -17.6) |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 5.11 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0362× (z -11.7) |
| [[SW480 (line)]] | alt | 3.50 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0271× (z -15.1) |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.4) |
| [[LoVo (line)]] | wt | 5.53 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0794× (z -9.9) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.0826× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -8.7) |
| [[A-172 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.369 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC4]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMEM125]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[ARHGAP30]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.72 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FUT3]] | +0.71 | +0.70 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[NECTIN4]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ERBB3]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |
| [[SPATA6L]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[USH1C]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RORC]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*118 arrows, 118 of them with an alert ⚠; grade A 0, B 15, C 103. Shown: the 12 strongest; 106 more arrows (106 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | DCLK2 activity lowers ADCY4's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.13× higher at baseline in the lines without DCLK2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[DZIP1L]] | B | DZIP1L activity lowers ADCY4's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.74× higher at baseline in the lines without DZIP1L | 0.015 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[TTC28]] | B | TTC28 activity lowers ADCY4's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.25× higher at baseline in the lines without TTC28 | 0.019 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[MUC20]] | B | MUC20 activity raises ADCY4's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without MUC20 | 0.031 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises ADCY4's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without SPATA6L | 0.035 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises ADCY4's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.09× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[FUT2]] | B | FUT2 activity raises ADCY4's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without FUT2 | 0.042 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises ADCY4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without EPS8L1 | 0.052 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[FGD3]] | B | FGD3 activity raises ADCY4's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.08× lower at baseline in the lines without FGD3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[PTPN22]] | B | PTPN22 activity raises ADCY4's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without PTPN22 | 0.058 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises ADCY4's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without MYO1D | 0.059 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[SDCBP2]] | B | SDCBP2 activity raises ADCY4's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.16× lower at baseline in the lines without SDCBP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |

### Downstream of this gene

*132 arrows, 132 of them with an alert ⚠; grade A 0, B 37, C 95. Shown: the 12 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDCBP2]] | B | ADCY4 activity raises SDCBP2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 5.19× lower at baseline in the lines without ADCY4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[FAM83E]] | B | ADCY4 activity raises FAM83E's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.75× lower at baseline in the lines without ADCY4 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[TLDC2]] | B | ADCY4 activity raises TLDC2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without ADCY4 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[SLC44A3]] | B | ADCY4 activity raises SLC44A3's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without ADCY4 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[MUC20]] | B | ADCY4 activity raises MUC20's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without ADCY4 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[MYO1D]] | B | ADCY4 activity raises MYO1D's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without ADCY4 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[DCLK2]] | B | ADCY4 activity lowers DCLK2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 4.46× higher at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[ARHGEF5]] | B | ADCY4 activity raises ARHGEF5's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[ARHGEF34P]] | B | ADCY4 activity raises ARHGEF34P's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[FUT2]] | B | ADCY4 activity raises FUT2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without ADCY4 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[MROH7]] | B | ADCY4 activity raises MROH7's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without ADCY4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[LINC01504]] | B | ADCY4 activity raises LINC01504's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 1.69× lower at baseline in the lines without ADCY4 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.7, 55.6); signed map (58.3, 6.2). **Vector** length 52.4, 18.3% of its response variance represented; |z| ≥ 3 in 332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -3.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,318,349-24,335,093 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC4 |
| Gene groups (HGNC) | Adenylate cyclases |
| Reactome | 42 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFM4](https://www.uniprot.org/uniprotkb/Q8NFM4) (Adenylate cyclase type 4):

> Catalyzes the formation of the signaling molecule cAMP in response to G protein signaling.

**Summary**, from NCBI Gene [196883](https://www.ncbi.nlm.nih.gov/gene/196883):

> This gene encodes a member of the family of adenylate cyclases, which are membrane-associated enzymes that catalyze the formation of the secondary messenger cyclic adenosine monophosphate (cAMP). Mouse studies show that adenylate cyclase 4, along with adenylate cyclases 2 and 3, is expressed in olfactory cilia, suggesting that several different adenylate cyclases may couple to olfactory receptors and that there may be multiple receptor-mediated mechanisms for the generation of cAMP signals. …

**Accessions** — [HGNC:235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:235) · Entrez [196883](https://www.ncbi.nlm.nih.gov/gene/196883) · UniProt [Q8NFM4](https://www.uniprot.org/uniprotkb/Q8NFM4) · Ensembl [ENSG00000129467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129467)

## Data

Gene col 4974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4974); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4974]; `tensor/DDL_lfc|DDL_z.npy` [4974]; `embed/gene_vectors.npy` [4974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4974 or target_col == 4974). Every well: [[ADCY4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
