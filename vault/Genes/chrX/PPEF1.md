---
symbol: "PPEF1"
type: "gene"
col: 1470
ensembl_id: "ENSG00000086717"
name: "protein phosphatase with EF-hand domain 1"
location: "Xp22.13"
module: 10
arm: "+"
pooled_cpm: 4.05
n_lines_expressing: 45
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PPEF1

*protein phosphatase with EF-hand domain 1* — Xp22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.72× (z +17.6, q 0e+00, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.421× (z -8.1, q 4e-13, down in 18 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.71, fdr 1e-05), [[LINC01569]] (+0.70, fdr 1e-05), [[MIR1915HG]] (+0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[P4HA3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +17.6 | 0e+00 | 20/26 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.39×** | +14.0 | 3e-42 | 4/9 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.7 | 2e-29 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +10.5 | 7e-24 | 12/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +10.4 | 2e-23 | 2/5 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.5 | 4e-06 | 8/23 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.3 | 8e-06 | 17/39 (BT-474, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +4.9 | 6e-05 | 11/31 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.7 | 2e-04 | 6/24 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.9 | 0.005 | 9/40 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.007 | 10/36 (NCI-H23, SW480, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.016 | 3/40 (SW480, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.048 | 4/34 (A549, A498, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.83× | +3.0 | 0.11 | 0/7 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.421×** | -8.1 | 4e-13 | 18/35 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -7.3 | 1e-10 | 21/41 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.625×** | -4.5 | 0.002 | 12/40 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -4.2 | 0.004 | 13/33 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.656×** | -4.0 | 0.007 | 13/34 (NCI-H460, A549, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -3.4 | 0.059 | 9/40 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.712×** | -3.2 | 0.087 | 10/40 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -3.2 | 0.087 | 8/19 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.091 | 11/38 (H4, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.7 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.190× (z -11.7) |
| [[A-172 (line)]] | wt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +8.9) | — |
| [[A549 (line)]] | wt | 9.16 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0898× (z -10.1) |
| [[C-33 A (line)]] | alt | 5.73 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.05 µM 0.0549× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 1.75 | 0 | 1 | — | [[Pimozide (drug)]] 5 µM 0.0520× (z -8.7) |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.71 | +0.80 / +0.51 | both halves | 1e-05 | pathway: Sensory Perception |
| [[LINC01569]] | +0.70 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[MIR1915HG]] | +0.67 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[CFAP54]] | +0.65 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[DENND5B-AS1]] | +0.65 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[CYP1B1-AS1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.64 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[LINC02026]] | +0.64 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[MEI1]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[SOCS3-DT]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TPRG1]] | +0.63 | +0.67 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPEF1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCA17P]] | B | ABCA17P activity raises PPEF1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without ABCA17P | 0.025 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises PPEF1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without MIR1915HG | 0.040 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[LRRC4B]] | B | LRRC4B activity raises PPEF1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without LRRC4B | 0.062 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[FTCDNL1]] | B | FTCDNL1 activity raises PPEF1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without FTCDNL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P4HA3]] | C | PPEF1's natural level weakens P4HA3's drug response | PPEF1's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.29; direction clear | 0.048 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.9, 28.9); signed map (36.1, -7.9). **Vector** length 50.9, 7.57% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +17.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +3.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -2.0 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase with EF-hand domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:18,675,909-18,827,921 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPP7CA; previously PPEF |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; EF-hand domain containing |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O14829](https://www.uniprot.org/uniprotkb/O14829) (Serine/threonine-protein phosphatase with EF-hands 1):

> Dephosphorylates and destabilises PDCD5 to inhibit TP53/p53-mediated signaling. May have a role in the recovery or adaptation response of photoreceptors (By similarity).

**Summary**, from NCBI Gene [5475](https://www.ncbi.nlm.nih.gov/gene/5475):

> This gene encodes a member of the serine/threonine protein phosphatase with EF-hand motif family. The protein contains a protein phosphatase catalytic domain, and at least two EF-hand calcium-binding motifs in its C terminus. Although its substrate(s) is unknown, the encoded protein has been suggested to play a role in specific sensory neuron function and/or development. This gene shares high sequence similarity with the Drosophila retinal degeneration C (rdgC) gene. Several alternatively …

**Accessions** — [HGNC:9243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9243) · Entrez [5475](https://www.ncbi.nlm.nih.gov/gene/5475) · UniProt [O14829](https://www.uniprot.org/uniprotkb/O14829) · Ensembl [ENSG00000086717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086717)

## Data

Gene col 1470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1470); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1470]; `tensor/DDL_lfc|DDL_z.npy` [1470]; `embed/gene_vectors.npy` [1470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1470 or target_col == 1470). Every well: [[PPEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
