---
symbol: "PGP"
type: "gene"
col: 11503
ensembl_id: "ENSG00000184207"
name: "phosphoglycolate phosphatase"
location: "16p13.3"
module: 36
arm: "+"
pooled_cpm: 5.77
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PGP

*phosphoglycolate phosphatase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.35× (z +12.2, q 5e-32, up in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +12.0, q 5e-31, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.612× (z -5.8, q 4e-06, down in 25 of 46 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ cell-cycle shift, explains ~53% of this change); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0405×); [[Tadalafil (drug)]] 5 µM in 1 line (SK-MEL-2 0.0709×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.253×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYCBP]] (+0.67, fdr 1e-05), [[FOXK2]] (+0.65, fdr 1e-05), [[SAP130]] (+0.64, fdr 6e-05); moves opposite to [[AIMP1]] (-0.62, fdr 1e-05), [[KPNA5]] (-0.59, fdr 1e-05), [[RRAGB]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **4.35×** | +12.2 | 5e-32 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **4.35×** | +12.2 | 5e-32 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +12.0 | 5e-31 | 40/40 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **3.80×** | +11.1 | 1e-26 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **3.04×** | +9.2 | 3e-18 | 26/28 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **3.05×** | +8.9 | 4e-17 | 8/10 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.41×** | +7.3 | 2e-11 | 30/40 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.31×** | +6.4 | 9e-09 | 11/16 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.95×** | +5.4 | 5e-06 | 22/39 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.92×** | +5.2 | 1e-05 | 17/31 (SW1417, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.90×** | +5.1 | 1e-05 | 24/42 (HT-29, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.89×** | +5.1 | 2e-05 | 18/33 (LS 180, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.76×** | +4.7 | 1e-04 | 13/29 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.65×** | +4.2 | 0.001 | 18/47 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 14/47 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.013 | 16/44 (A549, SW480, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +3.4 | 0.023 | 5/44 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.039 | 5/40 (HEC-1-A, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.093 | 10/45 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.100 | 10/46 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.41×** | +2.9 | 0.100 | 2/45 (A549, HOP62) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11503.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ cell-cycle shift, explains ~53% of this change); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0405×); [[Tadalafil (drug)]] 5 µM in 1 line (SK-MEL-2 0.0709×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.612×** | -5.8 | 4e-06 | 25/46 (A-427, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.523×** | -5.4 | 2e-05 | 23/43 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.667× | -3.4 | 0.14 | 17/43 (NCI-H2347, hTERT-HPNE, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.686× | -3.1 | 0.19 | 12/47 (CHP-212, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.687× | -3.1 | 0.19 | 14/46 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.774× | -3.0 | 0.23 | 17/47 (LS 180, SW48, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -8.6) |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.205× (z -9.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 6.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0405× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0709× (z -8.7) |
| [[SW480 (line)]] | alt | 5.59 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A498 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYCBP]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SAP130]] | +0.64 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[TRAPPC10]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HIRA]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PAQR4]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CMC2]] | +0.62 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ARPC5L]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SRGAP2C]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RAB5IF]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[EMC8]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[NUDT1]] | +0.60 | +0.34 / +0.66 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIMP1]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[KPNA5]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[RRAGB]] | -0.58 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[OCIAD1]] | -0.57 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[AMZ2P1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CHURC1]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[C1orf43]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[RAD52]] | -0.53 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[MATCAP2]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[BTN2A3P]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NDUFA5]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZNF385C]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PGP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CTXN1]] | B | CTXN1 activity raises PGP's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without CTXN1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises PGP's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without CDC25A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-27.6, -40.0); signed map (-47.6, -22.9). **Vector** length 69.0, 13.1% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +12.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | +12.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | +3.3 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.3 | +12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.8 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.3 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.7 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglycolate phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,211,593-2,214,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AUM, G3PP |
| Reactome | 3 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NDG6](https://www.uniprot.org/uniprotkb/A6NDG6) (Phosphoglycolate phosphatase):

> Phosphatase with activity against multiple substrates. Acts as a metabolite repair enzyme which eliminates toxic glycolytic side products. Dephosphorylates 2-phosphoglycolate which is generated during the repair of oxidative DNA lesions. This controls triosephosphate isomerase activity, glycerolipid partitioning and cell proliferation in the embryo and is required for embryonic development (By similarity). Dephosphorylates 4-phosphoerythronate, a side product which is produced following …

**Summary**, from NCBI Gene [283871](https://www.ncbi.nlm.nih.gov/gene/283871):

> Enables phosphoglycolate phosphatase activity and sn-glycerol 3-phosphatase activity. Involved in several processes, including glycerol biosynthetic process; negative regulation of gluconeogenesis; and toxic metabolite repair. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8909) · Entrez [283871](https://www.ncbi.nlm.nih.gov/gene/283871) · UniProt [A6NDG6](https://www.uniprot.org/uniprotkb/A6NDG6) · Ensembl [ENSG00000184207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184207)

## Data

Gene col 11503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11503); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11503]; `tensor/DDL_lfc|DDL_z.npy` [11503]; `embed/gene_vectors.npy` [11503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11503 or target_col == 11503). Every well: [[PGP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
