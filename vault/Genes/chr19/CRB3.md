---
symbol: "CRB3"
type: "gene"
col: 5081
ensembl_id: "ENSG00000130545"
name: "crumbs cell polarity complex component 3"
location: "19p13.3"
module: 12
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 21
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 14
direction_downstream: 26
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CRB3

*crumbs cell polarity complex component 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.05× (z +9.8, q 6e-20, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.89× (z +5.7, q 2e-06, up in 5 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Entecavir (monohydrate) (drug)]] 5 µM: 0.533× (z -3.8, q 0.078, down in 1 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.0965×; ⚠ toxic).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF223]] (+0.58, fdr 1e-05), [[ZSCAN16]] (+0.58, fdr 4e-05), [[OR7E38P]] (+0.53, fdr 9e-05); moves opposite to [[TXNDC5]] (-0.52, fdr 5e-05), [[STT3B]] (-0.48, fdr 4e-05), [[NUDT3]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CLDN7]] → it (grade C ⚠); 26 go from it, the strongest it → [[TMEM265]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +9.8 | 6e-20 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +8.9 | 2e-16 | 5/11 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +7.8 | 2e-12 | 1/5 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.89×** | +5.7 | 2e-06 | 5/19 (NCI-H1573, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.82×** | +5.3 | 1e-05 | 6/18 (AsPC-1, HT-29, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.07×** | +4.6 | 4e-04 | 4/13 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.4 | 1e-03 | 2/15 (HT-29, SW1417) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.2 | 0.002 | 1/15 (HCT15) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +3.8 | 0.010 | 1/14 (NCI-H1573) | top dose only | cell-cycle shift (explains ~25% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.7 | 0.010 | 1/14 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.7 | 0.012 | 0/16 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.12×** | +3.4 | 0.028 | 1/10 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.043 | 5/14 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.069 | 3/16 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.069 | 0/17 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5081.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.0965×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.533×** | -3.8 | 0.078 | 1/19 (NCI-H2030) | top dose only | plate-row cell shift; position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | 0.363× | -3.3 | 0.24 | 2/19 (SW480, HepG2/C3A) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 8.06 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0965× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF223]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ZSCAN16]] | +0.58 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[OR7E38P]] | +0.53 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[POLD4]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CLDN4]] | +0.53 | +0.35 / +0.55 | both halves | 1e-04 | pathway: HALLMARK_APICAL_JUNCTION |
| [[COA3]] | +0.53 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[CLDN3]] | +0.52 | +0.27 / +0.62 | both halves | 3e-04 | pathway: Cell junction organization; STRING 454 |
| [[DAPP1]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CHMP2B]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[POLR2J]] ⚠ | +0.52 | +0.38 / +0.50 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAL4]] | +0.51 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[TRAPPC5]] | +0.51 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[TMEM205]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.52 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[STT3B]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 | pathway: SARS-CoV-2 Infection |
| [[NUDT3]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RNPS1]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SENP3]] | -0.47 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[RBM14-RBM4]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[BIVM]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[WDR12]] | -0.46 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[GMPS]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[KCTD15]] | -0.44 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[TBC1D4]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PON2]] | -0.43 | -0.36 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN7]] | C | CLDN7 activity raises CRB3's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 4.21× lower at baseline in the lines without CLDN7 | 3e-05 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises CRB3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.88× lower at baseline in the lines without CLDN3 | 5e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises CRB3's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 3.98× lower at baseline in the lines without EPCAM | 8e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises CRB3's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without RNF39 | 9e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[RNF223]] | C | RNF223 activity raises CRB3's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 3.78× lower at baseline in the lines without RNF223 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2; co-absent with the target |
| [[AP1M2]] | C | AP1M2 activity raises CRB3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 3.23× lower at baseline in the lines without AP1M2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7; co-absent with the target |
| [[CLDN4]] | C | CLDN4 activity raises CRB3's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.37× lower at baseline in the lines without CLDN4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises CRB3's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.37× lower at baseline in the lines without DAPP1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[NECTIN4]] | C | NECTIN4 activity raises CRB3's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.90× lower at baseline in the lines without NECTIN4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25; co-absent with the target |
| [[CGN]] | C | CGN activity raises CRB3's level | lines that do not express CGN (21) vs lines expressing it (29) | 3.01× lower at baseline in the lines without CGN | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3; co-absent with the target |
| [[PDZK1IP1]] | C | PDZK1IP1 activity raises CRB3's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without PDZK1IP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises CRB3's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.83× lower at baseline in the lines without WFDC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 10, C 16. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM265]] | B | CRB3 activity raises TMEM265's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without CRB3 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[TRAF4]] | B | CRB3 activity raises TRAF4's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CRB3 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | CRB3, [[ENSG00000275234]] activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 0.83× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| [[CHMP2B]] | B | CRB3 activity raises CHMP2B's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without CRB3 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[NUDT14]] | B | CRB3 activity raises NUDT14's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CRB3 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | CRB3, [[ENSG00000275234]] activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 1.17× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | CRB3, [[ENSG00000275234]] activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 0.75× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | CRB3, [[ENSG00000275234]] activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 1.18× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | CRB3, [[ENSG00000275234]] activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 0.74× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | B | CRB3, [[ENSG00000275234]] activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express CRB3, ENSG00000275234 (29) vs lines expressing them (19) | the lines without CRB3, ENSG00000275234: 1.22× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent genes |
| [[EPCAM]] | C | CRB3 activity raises EPCAM's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 13.32× lower at baseline in the lines without CRB3 | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |
| [[CLDN7]] | C | CRB3 activity raises CLDN7's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 11.59× lower at baseline in the lines without CRB3 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-53.9, -3.9); signed map (-10.4, -3.2). **Vector** length 28.9, 5.65% of its response variance represented; |z| ≥ 3 in 243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +1.7 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +8.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | +1.5 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | crumbs cell polarity complex component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,463,777-6,467,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17303 |
| Gene groups (HGNC) | Crumbs complex components |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: SARS-CoV-2 targets PDZ proteins in cell-cell junction; Tight junction interactions; SARS-CoV-2-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUF7](https://www.uniprot.org/uniprotkb/Q9BUF7) (Protein crumbs homolog 3):

> Involved in the establishment of cell polarity in mammalian epithelial cells. Regulates the morphogenesis of tight junctions. Involved in promoting phosphorylation and cytoplasmic retention of transcriptional coactivators YAP1 and WWTR1/TAZ which leads to suppression of TGFB1-dependent transcription of target genes such as CCN2/CTGF, SERPINE1/PAI1, SNAI1/SNAIL1 and SMAD7 (By similarity).

**Summary**, from NCBI Gene [92359](https://www.ncbi.nlm.nih.gov/gene/92359):

> This gene encodes a member of the Crumbs family of proteins. This gene is widely expressed in epithelial tissues where the encoded protein isoforms play various roles such as the control of cytokinesis and ciliogenesis or the formation of tight junctions. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:20237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20237) · Entrez [92359](https://www.ncbi.nlm.nih.gov/gene/92359) · UniProt [Q9BUF7](https://www.uniprot.org/uniprotkb/Q9BUF7) · Ensembl [ENSG00000130545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130545)

## Data

Gene col 5081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5081); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5081]; `tensor/DDL_lfc|DDL_z.npy` [5081]; `embed/gene_vectors.npy` [5081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5081 or target_col == 5081). Every well: [[CRB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
