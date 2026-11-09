---
symbol: "SH3BP5"
type: "gene"
col: 5196
ensembl_id: "ENSG00000131370"
name: "SH3 domain binding protein 5"
location: "3p25.1"
module: 30
arm: "+"
pooled_cpm: 44.29
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SH3BP5

*SH3 domain binding protein 5* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.81× (z +10.7, q 6e-24, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.809× (z -5.4, q 4e-05, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAS4]] (+0.67, fdr 7e-06), [[CYRIA]] (+0.64, fdr 9e-06), [[C14orf132]] (+0.59, fdr 3e-05); moves opposite to [[NUP50]] (-0.52, fdr 3e-05), [[RPRD1B]] (-0.50, fdr 4e-05), [[C2CD3]] (-0.50, fdr 5e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00888-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +10.7 | 6e-24 | 32/43 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +9.9 | 1e-20 | 29/43 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +7.9 | 6e-13 | 26/44 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.4 | 2e-11 | 22/44 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.7 | 3e-09 | 28/44 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.0 | 2e-07 | 24/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 3e-06 | 20/44 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 8e-06 | 21/44 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.6 | 2e-04 | 16/44 (PANC-1, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.0 | 0.003 | 14/44 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.015 | 10/44 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.017 | 10/44 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.017 | 14/44 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.029 | 16/44 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.029 | 9/44 (SNU-1, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -5.4 | 4e-05 | 20/44 (A-172, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.0 | 1e-04 | 20/44 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.751×** | -5.0 | 1e-04 | 17/35 (A-172, A549, …) | top dose only | composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 0.857× | -3.9 | 0.013 | 12/44 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.807×** | -3.9 | 0.013 | 17/44 (A-172, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.824×** | -3.5 | 0.045 | 13/43 (LOX-IMVI, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.826×** | -3.2 | 0.095 | 4/44 (A-427, KATO III, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.716× | -3.1 | 0.12 | 10/30 (LOX-IMVI, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 380 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -11.5) |
| [[CHP-212 (line)]] | wt | 154 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 2.66× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.519× (z -8.8) |
| [[SW480 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 33.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.467× (z -9.0) |
| [[COLO 205 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +12.1) | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -9.9) |
| [[LoVo (line)]] | wt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.222× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 68.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 59.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.5) |
| [[SW 900 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.0) | — |
| [[A498 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS4]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CYRIA]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[C14orf132]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ADM]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MAST1]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[NDRG4]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[METRNL]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CDON]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TMOD1]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[GSDME]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP50]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RPRD1B]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[C2CD3]] | -0.50 | -0.53 / -0.24 | both halves | 5e-04 |  |
| [[XRCC5]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ATR]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZNF876P]] | -0.50 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[ATE1]] | -0.49 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[TOR1A]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[HCFC1]] | -0.48 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[PSME3]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZNF407]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888-1]] | B | LINC00888-1 activity raises SH3BP5's level | lines that do not express LINC00888-1 (7) vs lines expressing it (43) | 2.38× lower at baseline in the lines without LINC00888-1 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises SH3BP5's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MME]] | B | MME activity raises SH3BP5's level | lines that do not express MME (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without MME | 0.080 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (25.1, 0.3); signed map (-2.1, 20.4). **Vector** length 107, 25.2% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.6 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,254,353-15,341,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sab |
| Gene groups (HGNC) | SH3 domain binding protein 5 family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O60239](https://www.uniprot.org/uniprotkb/O60239) (SH3 domain-binding protein 5):

> Functions as a guanine nucleotide exchange factor (GEF) with specificity for RAB11A and RAB25. Inhibits the auto- and transphosphorylation activity of BTK. Plays a negative regulatory role in BTK-related cytoplasmic signaling in B-cells. May be involved in BCR-induced apoptotic cell death.

**Summary**, from NCBI Gene [9467](https://www.ncbi.nlm.nih.gov/gene/9467):

> Enables guanyl-nucleotide exchange factor activity and protein kinase inhibitor activity. Acts upstream of or within intracellular signal transduction. Located in cytoplasmic vesicle membrane and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10827) · Entrez [9467](https://www.ncbi.nlm.nih.gov/gene/9467) · UniProt [O60239](https://www.uniprot.org/uniprotkb/O60239) · Ensembl [ENSG00000131370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131370)

## Data

Gene col 5196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5196); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5196]; `tensor/DDL_lfc|DDL_z.npy` [5196]; `embed/gene_vectors.npy` [5196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5196 or target_col == 5196). Every well: [[SH3BP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
