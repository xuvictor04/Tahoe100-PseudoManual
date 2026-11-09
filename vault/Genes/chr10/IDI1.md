---
symbol: "IDI1"
type: "gene"
col: 847
ensembl_id: "ENSG00000067064"
name: "isopentenyl-diphosphate delta isomerase 1"
location: "10p15.3"
module: 86
arm: "+"
pooled_cpm: 58.81
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 10
n_dd_up_clean: 31
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# IDI1

*isopentenyl-diphosphate delta isomerase 1* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (10 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 2.66× (z +18.4, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Quinestrol (drug)]] 5 µM: 0.768× (z -5.0, q 2e-04, down in 26 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCS1]] (+0.86, fdr 7e-06), [[HMGCR]] (+0.83, fdr 7e-06), [[ACAT2]] (+0.80, fdr 7e-06); moves opposite to [[LYRM9]] (-0.34, fdr 3e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MSMO1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.66×** | +18.4 | 0e+00 | 45/49 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.55×** | +17.6 | 0e+00 | 47/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +15.5 | 0e+00 | 37/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +10.4 | 3e-23 | 40/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +10.3 | 1e-22 | 44/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +9.5 | 3e-19 | 42/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +9.3 | 7e-19 | 41/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +9.2 | 2e-18 | 37/49 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.90×** | +8.2 | 1e-14 | 41/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.82×** | +7.9 | 1e-13 | 39/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +7.4 | 7e-12 | 39/48 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.71×** | +6.8 | 4e-10 | 39/49 (hTERT-HPNE, HOP62, …) | top dose only | plate-row cell shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.65×** | +6.6 | 2e-09 | 30/48 (Panc 03.27, J82, …) | all doses, stronger at high dose | composition shift |
| [[Posaconazole (drug)]] 5 µM |  | **1.66×** | +6.5 | 4e-09 | 36/48 (HEC-1-A, AsPC-1, …) | rises with dose | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.3 | 8e-09 | 36/47 (SNU-423, HOP62, …) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.3 | 1e-08 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.38×** | +6.1 | 4e-08 | 38/48 (HEC-1-A, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Quinestrol (drug)]] 5 µM |  | **0.768×** | -5.0 | 2e-04 | 26/49 (KATO III, NCI-H1792, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -5.0 | 2e-04 | 34/47 (A-427, LS 180, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.799×** | -4.3 | 0.004 | 26/48 (C32, KATO III, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.725×** | -4.2 | 0.004 | 24/48 (KATO III, HCT15, …) | top dose only |  |
| [[Asciminib (drug)]] 5 µM |  | **0.735×** | -4.1 | 0.004 | 26/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.740×** | -4.0 | 0.005 | 26/48 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.735×** | -3.9 | 0.007 | 22/49 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.024 | 24/47 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.773×** | -3.5 | 0.034 | 22/48 (SW 1088, LS 180, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.3 | 0.052 | 2/49 (C-33 A, CHP-212) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -3.2 | 0.062 | 22/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.852× | -3.1 | 0.10 | 16/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.2 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +22.4) | — |
| [[LoVo (line)]] | wt | 54.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +23.6) | — |
| [[SW480 (line)]] | alt | 29.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.2) | — |
| [[A549 (line)]] | wt | 30.7 | 6 | 0 | [[Cepharanthine (drug)]] 5 µM 5.32× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 47.9 | 6 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 3.59× (z +14.1) | — |
| [[KATO III (line)]] | alt | 115 | 2 | 4 (1 ⚠) | [[Berbamine (drug)]] 5 µM 2.39× (z +9.2) | [[Quinestrol (drug)]] 5 µM 0.363× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 59.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 100 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +19.1) | — |
| [[A-172 (line)]] | wt | 41.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.0) | — |
| [[A-427 (line)]] | wt | 89.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -18.0) |
| [[A498 (line)]] | wt | 50.7 | 4 | 0 | [[Berbamine (drug)]] 5 µM 2.84× (z +14.0) | — |
| [[COLO 205 (line)]] | alt | 64.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 36.2 | 4 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.59× (z +17.5) | — |
| [[J82 (line)]] | alt | 72.3 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.27× (z +9.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 110 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 2.65× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 46.0 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 75.6 | 3 | 0 | [[Berbamine (drug)]] 5 µM 3.87× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +22.1) | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 44.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 45.6 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 3.30× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 37.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 49.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.18× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 108 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.40× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 48.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.74× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 97.1 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.47× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.70× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 35.1 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.91× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 66.9 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 34.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.14× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 71.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.4) | — |
| [[SW48 (line)]] | wt | 53.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +16.2) | — |
| [[C32 (line)]] | wt | 31.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +8.8) | — |
| [[H4 (line)]] | wt | 22.9 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 4.03× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 96.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +16.7) | — |
| [[AN3 CA (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCS1]] | +0.86 | +0.88 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 972 |
| [[HMGCR]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 926 |
| [[ACAT2]] | +0.80 | +0.83 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 828 |
| [[FDPS]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 994 |
| [[DHCR7]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 864 |
| [[CYP51A1]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 942 |
| [[EBP]] | +0.76 | +0.79 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 622 |
| [[MSMO1]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 926 |
| [[FDFT1]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 940 |
| [[INSIG1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 860 |
| [[SCD]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 403 |
| [[ACSS2]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 449 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM9]] | -0.34 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises IDI1's level | compounds that target ABL1: 3 of 6 lower it (Asciminib, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.8% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSMO1]] | C | IDI1's natural level strengthens MSMO1's drug response | IDI1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.44; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -49.1); signed map (-52.9, 32.5). **Vector** length 142, 51.2% of its response variance represented; |z| ≥ 3 in 1,660 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.69 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.63 to 7); *SREBP1 lipogenesis* (control, mean cos +0.62 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +12.5 | +17.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +11.2 | +18.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +7.6 | +7.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +6.5 | +6.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | +6.5 | +8.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.9 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | isopentenyl-diphosphate delta isomerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:1,039,152-1,049,119 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, BILE_ACID_METABOLISM, PEROXISOME, ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM, MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13907](https://www.uniprot.org/uniprotkb/Q13907) (Isopentenyl-diphosphate Delta-isomerase 1):

> Catalyzes the 1,3-allylic rearrangement of the homoallylic substrate isopentenyl (IPP) to its highly electrophilic allylic isomer, dimethylallyl diphosphate (DMAPP).

**Summary**, from NCBI Gene [3422](https://www.ncbi.nlm.nih.gov/gene/3422):

> IDI1 encodes a peroxisomally-localized enzyme that catalyzes the interconversion of isopentenyl diphosphate (IPP) to its highly electrophilic isomer, dimethylallyl diphosphate (DMAPP), which are the substrates for the successive reaction that results in the synthesis of farnesyl diphosphate and, ultimately, cholesterol. It has been shown in peroxisomal deficiency diseases such as Zellweger syndrome and neonatal adrenoleukodystrophy that there is reduction in IPP isomerase activity. [provided by …

**Accessions** — [HGNC:5387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5387) · Entrez [3422](https://www.ncbi.nlm.nih.gov/gene/3422) · UniProt [Q13907](https://www.uniprot.org/uniprotkb/Q13907) · Ensembl [ENSG00000067064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067064)

## Data

Gene col 847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 847); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 847]; `tensor/DDL_lfc|DDL_z.npy` [847]; `embed/gene_vectors.npy` [847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 847 or target_col == 847). Every well: [[IDI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
