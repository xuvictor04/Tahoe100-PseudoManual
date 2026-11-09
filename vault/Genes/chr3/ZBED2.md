---
symbol: "ZBED2"
type: "gene"
col: 10829
ensembl_id: "ENSG00000177494"
name: "zinc finger BED-type containing 2"
location: "3q13.13"
module: 31
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 11
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 20
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ZBED2

*zinc finger BED-type containing 2* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.57× (z +8.1, q 3e-13, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.04× (z +4.5, q 5e-04, up in 0 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.0454×, HEC-1-A 0.158×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.0463×, A-427 0.129×); [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.136×, HEC-1-A 0.0931×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF860]] (+0.59, fdr 1e-05), [[MST1R]] (+0.57, fdr 2e-05), [[CAPN14]] (+0.57, fdr 2e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ONECUT3]] → it (grade C ⚠); 20 go from it, the strongest it → [[PLCXD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.57×** | +8.1 | 3e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.66×** | +7.0 | 8e-10 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.73×** | +6.5 | 1e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +4.8 | 2e-04 | 0/4 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.88×** | +4.8 | 2e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +4.5 | 5e-04 | 0/10 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.82×** | +4.5 | 7e-04 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.90×** | +4.4 | 8e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.49×** | +4.1 | 0.002 | 0/7 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.38×** | +3.9 | 0.005 | 0/3 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.85×** | +3.9 | 0.005 | 0/6 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.8 | 0.006 | 3/5 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.03×** | +3.8 | 0.006 | 1/1 (A-427) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +3.7 | 0.008 | 0/5 | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +3.7 | 0.008 | 1/7 (A-427) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.00×** | +3.5 | 0.014 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.025 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.04×** | +3.2 | 0.040 | 1/5 (SW480) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.97×** | +3.0 | 0.065 | 0/4 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10829.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.0454×, HEC-1-A 0.158×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.0463×, A-427 0.129×); [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.136×, HEC-1-A 0.0931×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abiraterone acetate (drug)]] 0.5 µM |  | 0.467× | -3.5 | 0.25 | 1/10 (SW48) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.496× | -3.2 | 0.27 | 0/10 | inconsistent across doses |  |
| [[Econazole (drug)]] 0.5 µM |  | 0.508× | -3.1 | 0.27 | 1/10 (SW1417) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.483× | -3.1 | 0.27 | 0/10 | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 5 µM |  | 0.283× | -3.0 | 0.28 | 0/9 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0261× (z -13.7) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0886× (z -12.9) |
| [[A-427 (line)]] | wt | 76.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -9.9) |
| [[SW480 (line)]] | alt | 1.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0454× (z -11.8) |
| [[A-172 (line)]] | wt | 0.160 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.129 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.161 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.184 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.135 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.167 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.184 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF860]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MST1R]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CAPN14]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 | **novel candidate** |
| [[BLACAT1]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[LEMD1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.54 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[EPHA2-AS1]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GJB3]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PADI1]] | +0.54 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[SCEL]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[CASC19]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ONECUT3]] | C | ONECUT3 activity raises ZBED2's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without ONECUT3 | 0.029 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 6, C 14. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCXD2]] | B | ZBED2 activity raises PLCXD2's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without ZBED2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[LINC02595]] | B | ZBED2 activity raises LINC02595's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.80× lower at baseline in the lines without ZBED2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[ITGA6]] | B | ZBED2 activity raises ITGA6's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 3.57× lower at baseline in the lines without ZBED2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[BCL2L1]] | B | ZBED2 activity raises BCL2L1's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without ZBED2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[TGFA]] | B | ZBED2 activity raises TGFA's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 4.11× lower at baseline in the lines without ZBED2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[LEMD1]] | B | ZBED2 activity raises LEMD1's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without ZBED2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[MST1R]] | C | ZBED2 activity raises MST1R's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 5.10× lower at baseline in the lines without ZBED2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[KIAA0040]] | C | ZBED2 activity raises KIAA0040's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 6.35× lower at baseline in the lines without ZBED2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[DMKN]] | C | ZBED2 activity raises DMKN's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 4.28× lower at baseline in the lines without ZBED2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[ITGB4]] | C | ZBED2 activity raises ITGB4's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 6.99× lower at baseline in the lines without ZBED2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[C1orf116]] | C | ZBED2 activity raises C1orf116's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 6.42× lower at baseline in the lines without ZBED2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |
| [[KLK10]] | C | ZBED2 activity raises KLK10's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 7.92× lower at baseline in the lines without ZBED2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.439). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 51.8); signed map (3.8, 38.3). **Vector** length 27.1, 7.40% of its response variance represented; |z| ≥ 3 in 299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.7 | +0.4 |
|  | [[vincristine (drug)]] 5 µM |  | +0.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.6 | +3.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.5 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:111,592,900-111,595,346 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10796 |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTP6](https://www.uniprot.org/uniprotkb/Q9BTP6) (Zinc finger BED domain-containing protein 2):

> Transcriptional regulator which has intrinsic repressor activity and which competes with the transcriptional activator IRF1 for binding to the 5'-[CA]GAA[AC]C[CT]-3' consensus sequence in gene promoters. May thereby play a role in keratinocyte differentiation.

**Summary**, from NCBI Gene [79413](https://www.ncbi.nlm.nih.gov/gene/79413):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II and positive regulation of keratinocyte differentiation. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20710) · Entrez [79413](https://www.ncbi.nlm.nih.gov/gene/79413) · UniProt [Q9BTP6](https://www.uniprot.org/uniprotkb/Q9BTP6) · Ensembl [ENSG00000177494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177494)

## Data

Gene col 10829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10829); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10829]; `tensor/DDL_lfc|DDL_z.npy` [10829]; `embed/gene_vectors.npy` [10829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10829 or target_col == 10829). Every well: [[ZBED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
