---
symbol: "NOS3"
type: "gene"
col: 9016
ensembl_id: "ENSG00000164867"
name: "nitric oxide synthase 3"
location: "7q36.1"
module: 158
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 22
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# NOS3

*nitric oxide synthase 3* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.42× (z +19.5, q 0e+00, up in 11 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.131×); [[Cobimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0527×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF165]] (+0.56, fdr 6e-05), [[CD22]] (+0.55, fdr 1e-05), [[ICAM2]] (+0.54, fdr 2e-05); moves opposite to [[PPP2R5E]] (-0.52, fdr 4e-05), [[METTL9]] (-0.49, fdr 3e-05), [[TAF5]] (-0.48, fdr 1e-04).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[COL17A1]] → it (grade C ⚠); 3 go from it, the strongest it → [[PAN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.42×** | +19.5 | 0e+00 | 11/14 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.21×** | +14.3 | 5e-44 | 1/4 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.68×** | +12.6 | 5e-34 | 3/7 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.45×** | +10.1 | 8e-22 | 9/15 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +9.0 | 3e-17 | 2/5 (NCI-H2347, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.90×** | +8.7 | 4e-16 | 13/16 (LoVo, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.50×** | +7.5 | 7e-12 | 3/11 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.76×** | +5.9 | 3e-07 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 3/20 (NCI-H2347, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +4.5 | 3e-04 | 7/16 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.82×** | +4.4 | 5e-04 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.0 | 0.003 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.9 | 0.004 | 0/14 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.5 | 0.020 | 1/12 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.020 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.020 | 4/16 (KATO III, SW480, …) | rises with dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.020 | 0/15 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.4 | 0.021 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.028 | 0/12 | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.028 | 1/14 (KATO III) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.046 | 1/12 (KATO III) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.054 | 1/13 (COLO 205) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.69×** | +3.1 | 0.054 | 0/14 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.062 | 0/13 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.131×); [[Cobimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0527×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 46.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 4.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 6.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +8.6) | — |
| [[KATO III (line)]] | alt | 9.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +10.4) | — |
| [[LoVo (line)]] | wt | 1.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.6) | — |
| [[A-172 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.838 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF165]] | +0.56 | +0.38 / +0.66 | both halves | 6e-05 |  |
| [[CD22]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ICAM2]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[TRPV3]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[GLRX2]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[OSBP2]] | +0.50 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[LINC02930]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[PRKG2-AS1]] | +0.49 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ZNF554]] | +0.48 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ABCA13]] | +0.48 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[HYDIN]] | +0.48 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[SFR1]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 | pathway: Platelet homeostasis |
| [[METTL9]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TAF5]] | -0.48 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SMARCD2]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PIK3R4]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MLEC]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ATP5PF]] | -0.47 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[SETD3]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ACTL6A]] | -0.46 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[POU2F1]] | -0.44 | -0.38 / -0.36 | both halves | 1e-04 | pathway: ESR-mediated signaling |
| [[PARN]] | -0.44 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[UBL5]] | -0.44 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL17A1]] | C | COL17A1 activity raises NOS3's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without COL17A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[RNF223]] | C | RNF223 activity raises NOS3's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without RNF223 | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAN3]] | B | NOS3 activity raises PAN3's level | lines that do not express NOS3 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without NOS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ABO, GJB3, SYK |
| [[TRPV3]] | B | NOS3 activity raises TRPV3's level | lines that do not express NOS3 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without NOS3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABO, GJB3, SYK |
| [[COL17A1]] | C | NOS3 activity raises COL17A1's level | lines that do not express NOS3 (28) vs lines expressing it (22) | 5.03× lower at baseline in the lines without NOS3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ABO, GJB3, SYK; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.3, 0.5); signed map (2.8, 33.9). **Vector** length 33.5, 6.41% of its response variance represented; |z| ≥ 3 in 423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +19.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.6 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.5 | -2.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.5 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide synthase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:150,991,017-151,014,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ECNOS, eNOS |
| Gene groups (HGNC) | Flavoproteins; Nitric oxide synthase family |
| Reactome | 22 pathways, smallest: NOSTRIN mediated eNOS trafficking; Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; eNOS activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P29474](https://www.uniprot.org/uniprotkb/P29474) (Nitric oxide synthase 3):

> Produces nitric oxide (NO) which is implicated in vascular smooth muscle relaxation through a cGMP-mediated signal transduction pathway. NO mediates vascular endothelial growth factor (VEGF)-induced angiogenesis in coronary vessels and promotes blood clotting through the activation of platelets.; [Isoform eNOS13C]: Lacks eNOS activity, dominant-negative form that may down-regulate eNOS activity by forming heterodimers with isoform 1.

**Summary**, from NCBI Gene [4846](https://www.ncbi.nlm.nih.gov/gene/4846):

> Nitric oxide is a reactive free radical which acts as a biologic mediator in several processes, including neurotransmission and antimicrobial and antitumoral activities. Nitric oxide is synthesized from L-arginine by nitric oxide synthases. Variations in this gene are associated with susceptibility to coronary spasm. Alternative splicing and the use of alternative promoters results in multiple transcript variants. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:7876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7876) · Entrez [4846](https://www.ncbi.nlm.nih.gov/gene/4846) · UniProt [P29474](https://www.uniprot.org/uniprotkb/P29474) · Ensembl [ENSG00000164867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164867)

## Data

Gene col 9016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9016); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9016]; `tensor/DDL_lfc|DDL_z.npy` [9016]; `embed/gene_vectors.npy` [9016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9016 or target_col == 9016). Every well: [[NOS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
