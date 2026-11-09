---
symbol: "KLRC3"
type: "gene"
col: 13015
ensembl_id: "ENSG00000205810"
name: "killer cell lectin like receptor C3"
location: "12p13.2"
module: 223
arm: "+"
pooled_cpm: 4.53
n_lines_expressing: 23
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 21
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# KLRC3

*killer cell lectin like receptor C3* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.66× (z +22.2, q 0e+00, up in 15 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.577× (z -4.6, q 0.001, down in 13 of 21 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.565× (z -4.6, q 0.001, down in 8 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRC4-KLRK1]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRC2]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRK1]] (+0.90, fdr 7e-06, ⚠ same locus), [[BMP5]] (+0.70, fdr 7e-06), [[CXXC4]] (+0.67, fdr 7e-06), [[ID4]] (+0.62, fdr 1e-05); moves opposite to [[GPR89A]] (-0.53, fdr 2e-05), [[IL17RA]] (-0.53, fdr 3e-05), [[VPS53]] (-0.52, fdr 4e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLRC4-KLRK1]], [[KLRK1]] → it (grade C ⚠); 21 go from it, the strongest it → cells under [[Riluzole hydrochloride (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.66×** | +22.2 | 0e+00 | 15/18 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.56×** | +12.5 | 1e-33 | 9/17 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.66×** | +12.2 | 4e-32 | 17/20 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +11.1 | 2e-26 | 15/21 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +10.8 | 2e-25 | 1/8 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +10.7 | 1e-24 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.99×** | +10.6 | 3e-24 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.21×** | +9.6 | 5e-20 | 10/18 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +5.8 | 4e-07 | 3/21 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.5 | 3e-06 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 2/20 (NCI-H2030, SW 900) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +4.6 | 2e-04 | 6/20 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.6 | 2e-04 | 1/7 (NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.8 | 0.006 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +3.8 | 0.006 | 0/14 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.013 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.013 | 3/20 (AsPC-1, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.020 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.020 | 6/20 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.040 | 3/12 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.043 | 6/21 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +2.9 | 0.076 | 2/12 (SNU-1, SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -4.6 | 0.001 | 13/21 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.565×** | -4.6 | 0.001 | 8/20 (NCI-H23, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.724×** | -3.8 | 0.025 | 10/21 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.040 | 17/20 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.040 | 5/21 (NCI-H460, HCT15, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.662×** | -3.5 | 0.049 | 3/19 (SW 1271, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -3.4 | 0.049 | 11/19 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.672×** | -3.3 | 0.062 | 5/18 (NCI-H23, SW 1271, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.685× | -3.0 | 0.14 | 5/18 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.676× | -3.0 | 0.14 | 4/20 (HepG2/C3A, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 58.3 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0303× (z -17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.113× (z -11.5) |
| [[SW480 (line)]] | alt | 5.09 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.100× (z -9.5) |
| [[A-427 (line)]] | wt | 23.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +13.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.140× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 7.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.3) | [[Bortezomib (drug)]] 0.05 µM 0.195× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 2.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 1.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 141× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +10.3) | — |
| [[A-172 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRC4-KLRK1]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | ⚠ same locus (2.2 kb, same strand: neighbours can correlate without regulation) |
| [[KLRC2]] | +0.95 | +0.96 / +0.93 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (6.3 kb, same strand: neighbours can correlate without regulation) |
| [[KLRK1]] | +0.90 | +0.92 / +0.84 | both halves | 7e-06 | same gene group; STRING 878; ⚠ same locus (20.4 kb, same strand: neighbours can correlate without regulation) |
| [[BMP5]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[CXXC4]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ID4]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NR4A3]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[POGZ]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[BCL3]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CFAP300]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ID2-AS1]] | +0.55 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ARHGAP25]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[IL17RA]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[VPS53]] | -0.52 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RABEPK]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TNPO3]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC5]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[EPS15L1]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[SRD5A1]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CTDP1]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MFN1]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | C | KLRC4-KLRK1, KLRK1 activity raises KLRC3's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 4.66× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent with the target; co-absent genes |
| [[KLRC2]] | C | KLRC2 activity raises KLRC3's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 4.14× lower at baseline in the lines without KLRC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises KLRC3's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.43× lower at baseline in the lines without IGFL4 | 0.060 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[SPTB]] | C | SPTB activity raises KLRC3's level | lines that do not express SPTB (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without SPTB | 0.074 | ⚠ within organs, on part of the lines; also absent: MAP7, DMKN, ICA1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | KLRC3 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Econazole (drug)]] 0.5 µM | B | KLRC3 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.85× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[GNG4]] | B | KLRC3 activity raises GNG4's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without KLRC3 | 0.037 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[PRKG2]] | B | KLRC3 activity raises PRKG2's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without KLRC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[LINC01091]] | B | KLRC3 activity raises LINC01091's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without KLRC3 | 0.044 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Bendamustine (drug)]] 5 µM | B | KLRC3 activity lowers the cells' numbers under Bendamustine 5 µM (makes them more sensitive) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 1.16× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | KLRC3 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (makes them more sensitive) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | KLRC3 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | B | KLRC3 activity lowers the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 1.13× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | KLRC3 activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| cells under [[Glasdegib (drug)]] 5 µM | B | KLRC3 activity raises the cells' numbers under Glasdegib 5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.89× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4; cell counts less trustworthy |
| [[OLFM1]] | B | KLRC3 activity raises OLFM1's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without KLRC3 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.919). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.5, 33.6); signed map (51.2, 19.9). **Vector** length 54.8, 13.5% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +22.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor C3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,412,315-10,420,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NKG2-E |
| Gene groups (HGNC) | Killer cell lectin like receptors; C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07444](https://www.uniprot.org/uniprotkb/Q07444) (NKG2-E type II integral membrane protein):

> Plays a role as a receptor for the recognition of MHC class I HLA-E molecules by NK cells and some cytotoxic T-cells.

**Summary**, from NCBI Gene [3823](https://www.ncbi.nlm.nih.gov/gene/3823):

> Natural killer (NK) cells are lymphocytes that can mediate lysis of certain tumor cells and virus-infected cells without previous activation. They can also regulate specific humoral and cell-mediated immunity. NK cells preferentially express several calcium-dependent (C-type) lectins, which have been implicated in the regulation of NK cell function. KLRC3 is a member of the NKG2 group which are expressed primarily in natural killer (NK) cells and encodes a family of transmembrane proteins …

**Accessions** — [HGNC:6376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6376) · Entrez [3823](https://www.ncbi.nlm.nih.gov/gene/3823) · UniProt [Q07444](https://www.uniprot.org/uniprotkb/Q07444) · Ensembl [ENSG00000205810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205810)

## Data

Gene col 13015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13015); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13015]; `tensor/DDL_lfc|DDL_z.npy` [13015]; `embed/gene_vectors.npy` [13015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13015 or target_col == 13015). Every well: [[KLRC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
