---
symbol: "SHISAL1"
type: "gene"
col: 6254
ensembl_id: "ENSG00000138944"
name: "shisa like 1"
location: "22q13.31"
module: 14
arm: "+"
pooled_cpm: 4.61
n_lines_expressing: 20
n_dd_up: 25
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 18
direction_downstream: 32
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SHISAL1

*shisa like 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.19× (z +12.5, q 6e-33, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +10.2, q 4e-22, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.544× (z -5.7, q 6e-06, down in 10 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFN1]] (+0.74, fdr 7e-06), [[ROR1-AS1]] (+0.72, fdr 7e-06), [[SLAMF7]] (+0.69, fdr 7e-06); moves opposite to [[MT1X]] (-0.50, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ZNF469]] → it (grade B ⚠); 32 go from it, the strongest it → [[ZNF469]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +12.5 | 6e-33 | 4/6 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +12.1 | 4e-31 | 5/6 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +12.0 | 6e-31 | 5/10 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +10.2 | 4e-22 | 9/14 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.34×** | +5.7 | 1e-06 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.4 | 6e-06 | 2/13 (A549, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.4 | 1e-03 | 1/10 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.2 | 0.001 | 0/12 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.2 | 0.001 | 2/12 (HS-578T, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.008 | 3/16 (A498, SW 900, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.7 | 0.009 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.015 | 6/14 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.44×** | +3.5 | 0.023 | 0/13 | top dose only | position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.025 | 1/12 (SHP-77) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.3 | 0.031 | 3/13 (NCI-H460, A498, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.039 | 1/15 (A-172) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.039 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.040 | 2/16 (SHP-77, Hs 766T) | rises with dose | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.040 | 1/13 (A-172) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.079 | 2/12 (SW 900, RPMI-7951) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.094 | 5/17 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.098 | 2/13 (SHP-77, A-172) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.544×** | -5.7 | 6e-06 | 10/15 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.592×** | -4.9 | 3e-04 | 9/14 (NCI-H1792, H4, …) | all doses, flat | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.606×** | -4.7 | 5e-04 | 10/16 (HS-578T, H4, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -3.9 | 0.011 | 6/17 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -3.9 | 0.011 | 10/17 (NCI-H1792, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.671×** | -3.7 | 0.018 | 7/13 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **0.674×** | -3.7 | 0.018 | 4/16 (H4, A498, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.034 | 7/16 (NCI-H1792, Hs 766T, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.070 | 4/16 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.716×** | -3.1 | 0.094 | 5/16 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -3.1 | 0.094 | 10/17 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -3.1 | 0.094 | 9/16 (H4, NCI-H1792, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.535×** | -3.1 | 0.096 | 9/14 (NCI-H1792, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.795× | -3.0 | 0.10 | 5/16 (H4, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 48.6 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +14.4) | [[Belinostat (drug)]] 5 µM 0.135× (z -11.9) |
| [[A-172 (line)]] | wt | 7.13 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.0318× (z -14.6) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.110× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0667× (z -16.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 9.71 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0834× (z -12.9) |
| [[SW 900 (line)]] | alt | 5.86 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0746× (z -8.5) |
| [[A498 (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.5) | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0693× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.133× (z -9.7) |
| [[SNU-423 (line)]] | alt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +8.5) | — |
| [[A-427 (line)]] | wt | 0.894 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.305 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFN1]] | +0.74 | +0.67 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ROR1-AS1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SLAMF7]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MSC]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[IL6]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZNF469]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC01828]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC01435]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SIRLNT]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[NLGN4Y]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ABCC9]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RRAD]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | -0.50 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 1, C 17. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF469]] | B | ZNF469 activity raises SHISAL1's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without ZNF469 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[ANGPTL2]] | C | ANGPTL2 activity raises SHISAL1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without ANGPTL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises SHISAL1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.98× lower at baseline in the lines without C5orf46 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises SHISAL1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without CDH13 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises SHISAL1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.41× lower at baseline in the lines without LINC01411 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises SHISAL1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.69× lower at baseline in the lines without IRAG2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises SHISAL1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.05× lower at baseline in the lines without STEAP1B-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises SHISAL1's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without TNFRSF11B | 0.045 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises SHISAL1's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without IL1B | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |
| [[LINC02154]] | C | LINC02154 activity raises SHISAL1's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 2.61× lower at baseline in the lines without LINC02154 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[ITGBL1]] | C | ITGBL1 activity raises SHISAL1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.73× lower at baseline in the lines without ITGBL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[IGFN1]] | C | IGFN1 activity raises SHISAL1's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without IGFN1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 7, C 25. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF469]] | B | SHISAL1 activity raises ZNF469's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without SHISAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[ZMIZ1]] | B | SHISAL1 activity raises ZMIZ1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without SHISAL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[SLC22A4]] | B | SHISAL1 activity raises SLC22A4's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without SHISAL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[ABCA13]] | B | SHISAL1 activity raises ABCA13's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without SHISAL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[PTHLH]] | B | SHISAL1 activity raises PTHLH's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without SHISAL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[CADM1]] | B | SHISAL1 activity raises CADM1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 4.03× lower at baseline in the lines without SHISAL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[FGF2]] | B | SHISAL1 activity raises FGF2's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.47× lower at baseline in the lines without SHISAL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[IL1B]] | C | SHISAL1 activity raises IL1B's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.65× lower at baseline in the lines without SHISAL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[MAF]] | C | SHISAL1 activity raises MAF's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 4.09× lower at baseline in the lines without SHISAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[COL7A1]] | C | SHISAL1 activity raises COL7A1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without SHISAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[CDH11]] | C | SHISAL1 activity raises CDH11's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.83× lower at baseline in the lines without SHISAL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[ANXA8]] | C | SHISAL1 activity raises ANXA8's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.56× lower at baseline in the lines without SHISAL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.9, 21.3); signed map (38.9, 22.8). **Vector** length 53.9, 17.2% of its response variance represented; |z| ≥ 3 in 460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | shisa like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,243,665-44,312,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1644 |
| Matched by | ensembl_id |

UniProt [Q3SXP7](https://www.uniprot.org/uniprotkb/Q3SXP7) carries no function annotation.

**Summary**, from NCBI Gene [85352](https://www.ncbi.nlm.nih.gov/gene/85352):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29335) · Entrez [85352](https://www.ncbi.nlm.nih.gov/gene/85352) · UniProt [Q3SXP7](https://www.uniprot.org/uniprotkb/Q3SXP7) · Ensembl [ENSG00000138944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138944)

## Data

Gene col 6254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6254); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6254]; `tensor/DDL_lfc|DDL_z.npy` [6254]; `embed/gene_vectors.npy` [6254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6254 or target_col == 6254). Every well: [[SHISAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHISAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
