---
symbol: "ZCCHC3"
type: "gene"
col: 14492
ensembl_id: "ENSG00000247315"
name: "zinc finger CCHC-type containing 3"
location: "20p13"
module: 11
arm: "+"
pooled_cpm: 8.47
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZCCHC3

*zinc finger CCHC-type containing 3* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +7.6, q 2e-11, up in 31 of 43 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.99× (z +7.2, q 2e-10, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.325× (z -11.8, q 1e-29, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOHH]] (+0.78, fdr 7e-06), [[ZNF764]] (+0.77, fdr 7e-06), [[TOPORS]] (+0.75, fdr 7e-06); moves opposite to [[NDRG3]] (-0.67, fdr 1e-05), [[STRAP]] (-0.64, fdr 1e-05), [[MBOAT2]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.67×** | +7.6 | 2e-11 | 31/43 (KATO III, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 1e-10 | 34/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +7.2 | 2e-10 | 39/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.95×** | +6.7 | 3e-09 | 28/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 4e-09 | 30/44 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +6.5 | 9e-09 | 30/40 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.83×** | +6.3 | 2e-08 | 30/40 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.26×** | +6.1 | 9e-08 | 30/42 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +4.9 | 5e-05 | 26/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +4.8 | 1e-04 | 21/47 (SW480, HOP62, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +4.3 | 9e-04 | 20/40 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.004 | 15/42 (NCI-H460, NCI-H23, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 12/44 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.015 | 12/43 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +3.5 | 0.016 | 14/47 (SW480, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.039 | 14/44 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.039 | 6/46 (PANC-1, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.051 | 8/44 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.063 | 4/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.325×** | -11.8 | 1e-29 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -10.7 | 2e-24 | 47/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -10.1 | 6e-22 | 42/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.689×** | -5.6 | 4e-06 | 23/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.608×** | -5.3 | 2e-05 | 24/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.465×** | -3.9 | 0.007 | 13/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.93 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -10.4) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 5.49 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0907× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0913× (z -11.3) |
| [[KATO III (line)]] | alt | 7.30 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -9.7) |
| [[SNU-423 (line)]] | alt | 8.59 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -9.5) |
| [[SW1417 (line)]] | alt | 5.58 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0853× (z -8.8) |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOHH]] | +0.78 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.77 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[LATS1]] | +0.74 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[UNK]] | +0.71 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EID2]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.67 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[STRAP]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[MBOAT2]] | -0.63 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TMED7]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[OPA1]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[PAPSS1]] | -0.62 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TM9SF2]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZCCHC3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ZCCHC3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EID2]] | C | EID2 activity raises ZCCHC3's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.51× lower at baseline in the lines without EID2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.5, 6.8); signed map (4.3, -17.6). **Vector** length 85.3, 16.9% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.8 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +6.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:297,570-300,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1103G7.7; previously C20orf99 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUD5](https://www.uniprot.org/uniprotkb/Q9NUD5) (Zinc finger CCHC domain-containing protein 3):

> Nucleic acid-binding protein involved in innate immune response to DNA and RNA viruses. Binds DNA and RNA in the cytoplasm and acts by promoting recognition of viral nucleic acids by virus sensors, such as RIGI, IFIH1/MDA5 and CGAS. Acts as a co-sensor for recognition of double-stranded DNA (dsDNA) by cGAS in the cytoplasm, thereby playing a role in innate immune response to cytosolic dsDNA and DNA virus. Binds dsDNA and probably acts by promoting sensing of dsDNA by CGAS, leading to enhance …

**Summary**, from NCBI Gene [85364](https://www.ncbi.nlm.nih.gov/gene/85364):

> Enables double-stranded DNA binding activity. Involved in cellular response to exogenous dsRNA; detection of virus; and positive regulation of innate immune response. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16230) · Entrez [85364](https://www.ncbi.nlm.nih.gov/gene/85364) · UniProt [Q9NUD5](https://www.uniprot.org/uniprotkb/Q9NUD5) · Ensembl [ENSG00000247315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247315)

## Data

Gene col 14492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14492); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14492]; `tensor/DDL_lfc|DDL_z.npy` [14492]; `embed/gene_vectors.npy` [14492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14492 or target_col == 14492). Every well: [[ZCCHC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
