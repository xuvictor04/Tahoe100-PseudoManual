---
symbol: "DIABLO"
type: "gene"
col: 11485
ensembl_id: "ENSG00000184047"
name: "diablo IAP-binding mitochondrial protein"
location: "12q24.31"
module: 52
arm: "+"
pooled_cpm: 51.66
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DIABLO

*diablo IAP-binding mitochondrial protein* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.46× (z +12.6, q 7e-34, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.533× (z -12.3, q 9e-32, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.747× (z -5.7, q 1e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZKSCAN5]] (+0.70, fdr 7e-06), [[PRPF6]] (+0.69, fdr 7e-06), [[ZBTB48]] (+0.69, fdr 7e-06); moves opposite to [[NCKAP1]] (-0.72, fdr 7e-06), [[B3GALNT2]] (-0.58, fdr 6e-05), [[TNPO1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +12.6 | 7e-34 | 43/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.1 | 4e-26 | 35/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.7 | 5e-20 | 40/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +8.0 | 1e-13 | 35/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +8.0 | 1e-13 | 37/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +7.0 | 2e-10 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.9 | 6e-10 | 32/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 8e-09 | 32/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.4 | 8e-09 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 20/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 24/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.19× | +3.4 | 0.029 | 14/48 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.11 | 18/48 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -12.3 | 9e-32 | 40/49 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -12.2 | 1e-31 | 34/42 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -8.8 | 3e-16 | 29/44 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -8.2 | 3e-14 | 32/47 (C-33 A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.747×** | -5.7 | 1e-06 | 33/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -4.7 | 2e-04 | 25/49 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -4.3 | 0.001 | 22/48 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.7 | 0.014 | 22/48 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | 0.840× | -3.6 | 0.023 | 11/49 (BT-474, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.844× | -3.3 | 0.049 | 17/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -3.3 | 0.049 | 18/48 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.1 | 0.088 | 12/48 (NCI-H661, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.2 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.8) | — |
| [[SW480 (line)]] | alt | 46.5 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 70.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 71.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.387× (z -12.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 47.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.168× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | — |
| [[A549 (line)]] | wt | 66.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -14.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0667× (z -10.5) |
| [[LoVo (line)]] | wt | 56.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 47.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.43× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 64.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0640× (z -18.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 90.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 48.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -17.8) ⚠ toxic |
| [[C32 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 72.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 48.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.88× (z +9.3) | — |
| [[KATO III (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0485× (z -23.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.359× (z -12.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0994× (z -12.2) |
| [[SW 900 (line)]] | alt | 62.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN5]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PRPF6]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZBTB48]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[EDC3]] | +0.64 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ASCC2]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[ZNF7]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DDX19A]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FAF2]] | +0.61 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[RGP1]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[DDX50]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GON4L]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.72 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[B3GALNT2]] | -0.58 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[TNPO1]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[HDAC2]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TMEM64]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DIABLO's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-34.9, -5.7); signed map (-14.7, -11.6). **Vector** length 93.3, 23.1% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +12.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.8 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.3 | -12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | diablo IAP-binding mitochondrial protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,207,668-122,226,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMAC, DIABLO-S, FLJ25049, FLJ10537, DFNA64 |
| Hallmark sets | APOPTOSIS |
| Reactome | 11 pathways, smallest: Release of apoptotic factors from the mitochondria; SMAC (DIABLO) binds to IAPs; SMAC(DIABLO)-mediated dissociation of IAP:caspase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR28](https://www.uniprot.org/uniprotkb/Q9NR28) (Diablo IAP-binding mitochondrial protein):

> Promotes apoptosis by activating caspases in the cytochrome c/Apaf-1/caspase-9 pathway. Acts by opposing the inhibitory activity of inhibitor of apoptosis proteins (IAP). Inhibits the activity of BIRC6/BRUCE by inhibiting its binding to caspases.; [Isoform 3]: Attenuates the stability and apoptosis-inhibiting activity of XIAP/BIRC4 by promoting XIAP/BIRC4 ubiquitination and degradation through the ubiquitin-proteasome pathway. Also disrupts XIAP/BIRC4 interacting with processed caspase-9 and …

**Summary**, from NCBI Gene [56616](https://www.ncbi.nlm.nih.gov/gene/56616):

> This gene encodes an inhibitor of apoptosis protein (IAP)-binding protein. The encoded mitochondrial protein enters the cytosol when cells undergo apoptosis, and allows activation of caspases by binding to inhibitor of apoptosis proteins. Overexpression of the encoded protein sensitizes tumor cells to apoptosis. A mutation in this gene is associated with young-adult onset of nonsyndromic deafness-64. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:21528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21528) · Entrez [56616](https://www.ncbi.nlm.nih.gov/gene/56616) · UniProt [Q9NR28](https://www.uniprot.org/uniprotkb/Q9NR28) · Ensembl [ENSG00000184047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184047)

## Data

Gene col 11485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11485); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11485]; `tensor/DDL_lfc|DDL_z.npy` [11485]; `embed/gene_vectors.npy` [11485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11485 or target_col == 11485). Every well: [[DIABLO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIABLO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
