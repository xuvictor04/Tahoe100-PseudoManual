---
symbol: "DNAJC25"
type: "gene"
col: 679
ensembl_id: "ENSG00000059769"
name: "DnaJ heat shock protein family (Hsp40) member C25"
location: "9q31.3"
module: 49
arm: "+"
pooled_cpm: 77.84
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# DNAJC25

*DnaJ heat shock protein family (Hsp40) member C25* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.93× (z +7.5, q 3e-11, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.528× (z -7.0, q 1e-09, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM: 0.637× (z -5.1, q 8e-05, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.84, fdr 7e-06), [[PGM3]] (+0.82, fdr 7e-06), [[SERP1]] (+0.78, fdr 7e-06); moves opposite to [[UBE2E3]] (-0.63, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CADPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +7.5 | 3e-11 | 39/48 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +6.8 | 3e-09 | 36/48 (LoVo, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.6 | 8e-09 | 39/49 (AsPC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +5.7 | 2e-06 | 41/49 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +4.9 | 1e-04 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +4.6 | 3e-04 | 35/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 30/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.6 | 3e-04 | 30/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.064 | 28/48 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.072 | 21/49 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.072 | 23/48 (LoVo, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.074 | 24/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.098 | 21/49 (MIA PaCa-2, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -7.0 | 1e-09 | 32/40 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.637×** | -5.1 | 8e-05 | 38/49 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.642×** | -5.0 | 8e-05 | 39/49 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -5.0 | 8e-05 | 32/49 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.649×** | -4.9 | 1e-04 | 37/48 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.655×** | -4.8 | 1e-04 | 35/48 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.661×** | -4.7 | 2e-04 | 37/49 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.661×** | -4.7 | 2e-04 | 36/48 (SW 900, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.656×** | -4.6 | 3e-04 | 32/48 (J82, NCI-H2347, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.678×** | -4.4 | 6e-04 | 32/49 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.682×** | -4.4 | 7e-04 | 32/49 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.694×** | -4.2 | 0.002 | 35/48 (HT-29, H4, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.716×** | -3.8 | 0.006 | 29/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -3.5 | 0.017 | 25/44 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.017 | 24/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.017 | 28/48 (C32, LoVo, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.737×** | -3.2 | 0.051 | 21/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.757×** | -3.1 | 0.051 | 22/48 (LS 180, COLO 205, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 82.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 59.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 74.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -14.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 54.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +9.8) | — |
| [[A-427 (line)]] | wt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 67.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 73.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 93.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[RKO (line)]] | wt | 64.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 98.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 76.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.0) | — |
| [[A-172 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[PGM3]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[SERP1]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[EAF2]] | +0.78 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.77 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SLC15A2]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2E3]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises DNAJC25's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without CADPS2 | 0.063 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, -35.2); signed map (-50.8, 12.3). **Vector** length 120, 42.1% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.60 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.60 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.60 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | +4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.1 | -4.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -4.0 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.6 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,631,334-111,654,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA16L21.2.1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

UniProt [Q9H1X3](https://www.uniprot.org/uniprotkb/Q9H1X3) carries no function annotation.

**Summary**, from NCBI Gene [548645](https://www.ncbi.nlm.nih.gov/gene/548645):

> Predicted to be involved in protein folding. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34187) · Entrez [548645](https://www.ncbi.nlm.nih.gov/gene/548645) · UniProt [Q9H1X3](https://www.uniprot.org/uniprotkb/Q9H1X3) · Ensembl [ENSG00000059769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059769)

## Data

Gene col 679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 679); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 679]; `tensor/DDL_lfc|DDL_z.npy` [679]; `embed/gene_vectors.npy` [679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 679 or target_col == 679). Every well: [[DNAJC25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
