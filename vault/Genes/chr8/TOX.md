---
symbol: "TOX"
type: "gene"
col: 12706
ensembl_id: "ENSG00000198846"
name: "thymocyte selection associated high mobility group box"
location: "8q12.1"
module: 9
arm: "+"
pooled_cpm: 45.14
n_lines_expressing: 20
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TOX

*thymocyte selection associated high mobility group box* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +17.0, q 0e+00, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.537× (z -9.1, q 8e-17, down in 14 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSR1]] (+0.66, fdr 1e-05), [[ADAMTS1]] (+0.65, fdr 1e-05), [[ZNF804A]] (+0.60, fdr 1e-05); moves opposite to [[DENND3]] (-0.50, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[BAALC]] → it (grade C ⚠); 11 go from it, the strongest it → [[NRXN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +17.0 | 0e+00 | 5/18 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +11.6 | 8e-29 | 1/17 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +7.9 | 5e-13 | 6/17 (HOP62, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.5 | 1e-08 | 1/16 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.9 | 3e-07 | 5/18 (Panc 03.27, HOP62, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.3 | 1e-05 | 3/18 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 5/17 (LS 180, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.007 | 3/17 (SHP-77, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.008 | 12/18 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.008 | 4/18 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 1/19 (NCI-H1792) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.5 | 0.020 | 4/17 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.032 | 0/17 | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.072 | 4/16 (J82, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.096 | 3/18 (A-172, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.096 | 5/18 (HOP62, HS-578T, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.096 | 1/17 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -9.1 | 8e-17 | 14/17 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.560×** | -8.4 | 1e-14 | 18/18 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.571×** | -8.2 | 7e-14 | 16/18 (SHP-77, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.032 | 10/17 (NCI-H1792, Hs 766T, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.058 | 5/18 (SHP-77, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.058 | 10/18 (SHP-77, LS 180, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.058 | 0/18 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.852× | -3.3 | 0.058 | 12/18 (SHP-77, PANC-1, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.058 | 8/17 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.059 | 10/17 (SHP-77, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.661×** | -3.1 | 0.084 | 14/19 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.671× | -3.0 | 0.10 | 7/17 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.812× | -3.0 | 0.10 | 9/18 (SNU-423, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 497 | 0 | 16 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -21.4) |
| [[LS 180 (line)]] | wt | 107 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.205× (z -11.7) |
| [[C-33 A (line)]] | alt | 1,040 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.108× (z -18.3) |
| [[PANC-1 (line)]] | alt | 48.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.142× (z -9.3) |
| [[A-172 (line)]] | wt | 171 | 1 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 2.56× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 71.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -22.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 208 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -9.8) |
| [[HOP62 (line)]] | alt | 24.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 58.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -11.1) |
| [[Hs 766T (line)]] | wt | 51.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.4) |
| [[J82 (line)]] | alt | 105 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 406 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +8.9) | — |
| [[A-427 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSR1]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS1]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ZNF804A]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ROR1-AS1]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CDH12]] | +0.58 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[LINC01695]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[OFCC1]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CACNB2]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SOX5]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ABCA13]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NPFFR2]] | +0.56 | +0.33 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND3]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAALC]] | C | BAALC activity raises TOX's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without BAALC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises TOX's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without LINC02438 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises TOX's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.12× lower at baseline in the lines without PCDH18 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises TOX's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 7.11× lower at baseline in the lines without CDH6 | 0.018 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises TOX's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.43× lower at baseline in the lines without ASCL1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises TOX's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 5.30× lower at baseline in the lines without SHISAL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises TOX's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.13× lower at baseline in the lines without LINC01592 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises TOX's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without MSR1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN1]] | B | TOX activity raises NRXN1's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.80× lower at baseline in the lines without TOX | 0.065 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5 |
| [[LSAMP]] | B | TOX activity raises LSAMP's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.41× lower at baseline in the lines without TOX | 0.089 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5 |
| [[ZNF385D]] | C | TOX activity raises ZNF385D's level | lines that do not express TOX (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without TOX | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[SLIT2]] | C | TOX activity raises SLIT2's level | lines that do not express TOX (30) vs lines expressing it (20) | 4.26× lower at baseline in the lines without TOX | 0.053 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[SNTG1]] | C | TOX activity raises SNTG1's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.97× lower at baseline in the lines without TOX | 0.053 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[NTNG1]] | C | TOX activity raises NTNG1's level | lines that do not express TOX (30) vs lines expressing it (20) | 2.83× lower at baseline in the lines without TOX | 0.055 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[POU6F2]] | C | TOX activity raises POU6F2's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without TOX | 0.080 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[CDH6]] | C | TOX activity raises CDH6's level | lines that do not express TOX (30) vs lines expressing it (20) | 4.16× lower at baseline in the lines without TOX | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[RUNX1T1]] | C | TOX activity raises RUNX1T1's level | lines that do not express TOX (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without TOX | 0.087 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[TRPM8]] | C | TOX activity raises TRPM8's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.09× lower at baseline in the lines without TOX | 0.087 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[LINC02197]] | C | TOX activity raises LINC02197's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without TOX | 0.093 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.8, 26.1); signed map (39.8, 28.9). **Vector** length 72.5, 22.2% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | thymocyte selection associated high mobility group box |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:58,805,412-59,119,147 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0808, TOX1 |
| Gene groups (HGNC) | thymocyte selection associated high mobility group box family |
| Matched by | ensembl_id |

**Function**, from UniProt [O94900](https://www.uniprot.org/uniprotkb/O94900) (Thymocyte selection-associated high mobility group box protein TOX):

> Transcriptional regulator with a major role in neural stem cell commitment and corticogenesis as well as in lymphoid cell development and lymphoid tissue organogenesis (By similarity). Binds to GC-rich DNA sequences in the proximity of transcription start sites and may alter chromatin structure, modifying access of transcription factors to DNA. During cortical development, controls the neural stem cell pool by inhibiting the switch from proliferative to differentiating progenitors. Beyond …

**Summary**, from NCBI Gene [9760](https://www.ncbi.nlm.nih.gov/gene/9760):

> The protein encoded by this gene contains a HMG box DNA binding domain. HMG boxes are found in many eukaryotic proteins involved in chromatin assembly, transcription and replication. This protein may function to regulate T-cell development.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:18988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18988) · Entrez [9760](https://www.ncbi.nlm.nih.gov/gene/9760) · UniProt [O94900](https://www.uniprot.org/uniprotkb/O94900) · Ensembl [ENSG00000198846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198846)

## Data

Gene col 12706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12706); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12706]; `tensor/DDL_lfc|DDL_z.npy` [12706]; `embed/gene_vectors.npy` [12706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12706 or target_col == 12706). Every well: [[TOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
