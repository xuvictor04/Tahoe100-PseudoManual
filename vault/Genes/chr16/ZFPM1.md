---
symbol: "ZFPM1"
type: "gene"
col: 11045
ensembl_id: "ENSG00000179588"
name: "zinc finger protein, FOG family member 1"
location: "16q24.2"
module: 2
arm: "+"
pooled_cpm: 18.85
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZFPM1

*zinc finger protein, FOG family member 1* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.59× (z +12.5, q 7e-33, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.587× (z -7.0, q 1e-09, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.469× (z -5.2, q 3e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH1]] (+0.70, fdr 7e-06), [[TTYH3]] (+0.61, fdr 1e-05), [[VAV2]] (+0.60, fdr 1e-05); moves opposite to [[FIGN]] (-0.51, fdr 2e-05), [[DIS3L]] (-0.50, fdr 4e-05), [[PGGT1B]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GLS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +12.5 | 7e-33 | 45/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +7.2 | 2e-10 | 30/48 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +7.0 | 6e-10 | 33/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +6.5 | 1e-08 | 27/46 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 8e-08 | 27/48 (RKO, NCI-H460, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.037 | 8/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.31×** | +3.4 | 0.060 | 15/47 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.13 | 13/44 (HCT15, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -7.0 | 1e-09 | 27/38 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -6.9 | 1e-09 | 22/34 (LS 180, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.594×** | -6.5 | 1e-08 | 28/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -5.7 | 1e-06 | 21/32 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -5.2 | 3e-05 | 21/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.5 | 7e-04 | 25/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.003 | 19/47 (AN3 CA, LS 180, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.734×** | -4.0 | 0.004 | 14/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.738×** | -4.0 | 0.005 | 13/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.753×** | -3.7 | 0.013 | 17/44 (NCI-H23, J82, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.769×** | -3.3 | 0.051 | 18/42 (A-427, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.841× | -3.2 | 0.068 | 18/47 (hTERT-HPNE, A-172, …) | two highest doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0924× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 16.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.85× (z +9.0) | — |
| [[A549 (line)]] | wt | 25.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +11.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +9.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.00× (z +8.8) | — |
| [[LoVo (line)]] | wt | 16.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +14.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0829× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.135× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.135× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -11.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.1 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.199× (z -10.0) |
| [[KATO III (line)]] | alt | 25.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 | same gene group |
| [[TTYH3]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[VAV2]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RBM38]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PI4KAP2]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 | same gene group |
| [[ADCK5]] | +0.56 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NSMF]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 | same gene group |
| [[JAG2]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[INPP5A]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MIR3659HG]] | +0.54 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[PLCB3]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DIS3L]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PGGT1B]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[USP47]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZNF280D]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 | same gene group |
| [[CC2D2A]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ANGPT1]] | -0.47 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[POLR3C]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[AASDHPPT]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[TMEM126B]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ASF1A]] | -0.46 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CUL5]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLS2]] | B | GLS2 activity lowers ZFPM1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without GLS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[GRTP1]] | B | GRTP1 activity lowers ZFPM1's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 1.35× higher at baseline in the lines without GRTP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[HDAC6]] | B | HDAC6 activity lowers ZFPM1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens ZFPM1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.82× as strongly (z diff +0.42); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.22x vs 2.88x (z diff +3.8) | 0.359 over the table, 0.015 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (16.6, -5.7); signed map (-16.1, 34.3). **Vector** length 102, 23.7% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +7.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.9 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.8 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.5 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein, FOG family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:88,453,280-88,537,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRDM18, FOG1, FOG, ZNF89A |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; MicroRNA protein coding host genes; Zinc fingers FOG C2HC-type; Putative lysine methyltransferases |
| Reactome | 4 pathways, smallest: RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function; Factors involved in megakaryocyte development and platelet production; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX07](https://www.uniprot.org/uniprotkb/Q8IX07) (Zinc finger protein ZFPM1):

> Transcription regulator that plays an essential role in erythroid and megakaryocytic cell differentiation. Essential cofactor that acts via the formation of a heterodimer with transcription factors of the GATA family GATA1, GATA2 and GATA3. Such heterodimer can both activate or repress transcriptional activity, depending on the cell and promoter context. The heterodimer formed with GATA proteins is essential to activate expression of genes such as NFE2, ITGA2B, alpha- and beta-globin, while it …

**Summary**, from NCBI Gene [161882](https://www.ncbi.nlm.nih.gov/gene/161882):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity and transcription corepressor activity. Involved in platelet formation; regulation of definitive erythrocyte differentiation; and regulation of gene expression. Part of transcription repressor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19762) · Entrez [161882](https://www.ncbi.nlm.nih.gov/gene/161882) · UniProt [Q8IX07](https://www.uniprot.org/uniprotkb/Q8IX07) · Ensembl [ENSG00000179588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179588)

## Data

Gene col 11045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11045); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11045]; `tensor/DDL_lfc|DDL_z.npy` [11045]; `embed/gene_vectors.npy` [11045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11045 or target_col == 11045). Every well: [[ZFPM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFPM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
