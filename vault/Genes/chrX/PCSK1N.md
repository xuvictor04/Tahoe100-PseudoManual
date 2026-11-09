---
symbol: "PCSK1N"
type: "gene"
col: 2216
ensembl_id: "ENSG00000102109"
name: "proprotein convertase subtilisin/kexin type 1 inhibitor"
location: "Xp11.23"
module: 48
arm: "+"
pooled_cpm: 3.77
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# PCSK1N

*proprotein convertase subtilisin/kexin type 1 inhibitor* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.74× (z +8.9, q 4e-16, up in 14 of 15 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.77× (z +3.2, q 0.061, up in 10 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.406× (z -5.1, q 2e-04, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf48]] (+0.78, fdr 7e-06), [[LAMTOR2]] (+0.74, fdr 8e-06), [[RABAC1]] (+0.74, fdr 7e-06); moves opposite to [[GTF2H3]] (-0.63, fdr 2e-05), [[MAPKAPK5]] (-0.63, fdr 4e-05), [[GUF1]] (-0.62, fdr 6e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 7 go from it, the strongest it → [[GUF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.74×** | +8.9 | 4e-16 | 14/15 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.62×** | +7.1 | 5e-10 | 3/4 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.89×** | +5.6 | 4e-06 | 8/10 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.03×** | +4.0 | 0.007 | 15/25 (PANC-1, SW480, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.0 | 0.007 | 11/15 (CFPAC-1, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.97×** | +3.9 | 0.010 | 8/18 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.92×** | +3.7 | 0.015 | 12/26 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.82×** | +3.4 | 0.044 | 11/26 (PANC-1, SW480, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.78×** | +3.3 | 0.061 | 11/26 (PANC-1, SW480, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +3.2 | 0.061 | 10/22 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.061 | 10/25 (PANC-1, HOP62, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.74× | +3.0 | 0.11 | 6/24 (A-172, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.406×** | -5.1 | 2e-04 | 14/22 (SW 900, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.467×** | -4.3 | 0.004 | 12/25 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.312×** | -3.5 | 0.081 | 10/27 (SHP-77, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.548×** | -3.4 | 0.081 | 11/26 (NCI-H23, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.656×** | -3.4 | 0.081 | 13/21 (NCI-H2347, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.559×** | -3.3 | 0.091 | 11/23 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.341× | -3.2 | 0.11 | 11/22 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | 0.361× | -3.0 | 0.18 | 5/27 (AN3 CA, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 4.99 | 0 | 1 | — | [[Neratinib (drug)]] 0.5 µM 0.0401× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.1) |
| [[A-172 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf48]] | +0.78 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[LAMTOR2]] | +0.74 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[RABAC1]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[EGFL7]] | +0.73 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[COX6A1]] | +0.73 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[UBL5]] | +0.69 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[COX6C]] | +0.69 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.68 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ANAPC11]] | +0.68 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[TMEM256]] | +0.68 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[UQCRQ]] ⚠ | +0.67 | +0.52 / +0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[METRN]] | +0.67 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[COX7C]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.63 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.63 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[GUF1]] | -0.62 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[MTHFSD]] | -0.59 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[DARS2]] | -0.59 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[ELK4]] | -0.59 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[KRR1]] | -0.58 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ADSS2]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | -0.58 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.57 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PCSK1N's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PCSK1N's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GUF1]] | B | PCSK1N activity raises GUF1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.09× lower at baseline in the lines without PCSK1N | 0.005 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[DPM3]] | B | PCSK1N activity lowers DPM3's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.13× higher at baseline in the lines without PCSK1N | 0.019 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[ARSA]] | B | PCSK1N activity lowers ARSA's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.11× higher at baseline in the lines without PCSK1N | 0.029 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[NDUFB11]] | B | PCSK1N activity raises NDUFB11's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.12× lower at baseline in the lines without PCSK1N | 0.042 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[HCFC1R1]] | B | PCSK1N activity raises HCFC1R1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.03× lower at baseline in the lines without PCSK1N | 0.050 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | B | PCSK1N activity lowers the cells' numbers under Ouabain (Octahydrate) 0.05 µM (makes them more sensitive) | lines that do not express PCSK1N (21) vs lines expressing it (27) | the lines without PCSK1N: 1.08× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[GBF1]] | B | PCSK1N activity lowers GBF1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without PCSK1N | 0.095 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.9, -20.5); signed map (-33.5, 9.6). **Vector** length 38.6, 7.97% of its response variance represented; |z| ≥ 3 in 361 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.55 to 31); *Respiratory electron transport* (reactome, mean cos +0.55 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.56 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.4 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 1 inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,831,096-48,835,610 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAAS, SgVIII, SCG8, proSAAS, PEN, BigLEN |
| Gene groups (HGNC) | Granins |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHG2](https://www.uniprot.org/uniprotkb/Q9UHG2) (ProSAAS):

> May act as a protein chaperone that prevents the aggregation of client proteins and plays a role in neuroprotection. Blocks the trans-synaptic spread of SNCA/alpha-synuclein in the brain. May form spheres that encapsulate client proteins (By similarity). May prevent aggregation of amyloid beta, IAPP/islet amyloid polypeptide, and SNCA/alpha-synuclein. Cannot disaggregate preformed fibrils. Additionally, may function in the control of the neuroendocrine secretory pathway by acting as a specific …

**Summary**, from NCBI Gene [27344](https://www.ncbi.nlm.nih.gov/gene/27344):

> The protein encoded by this gene functions as an inhibitor of prohormone convertase 1, which regulates the proteolytic cleavage of neuroendocrine peptide precursors. The proprotein is further processed into multiple short peptides. A polymorphism within this gene may be associated with obesity. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:17301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17301) · Entrez [27344](https://www.ncbi.nlm.nih.gov/gene/27344) · UniProt [Q9UHG2](https://www.uniprot.org/uniprotkb/Q9UHG2) · Ensembl [ENSG00000102109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102109)

## Data

Gene col 2216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2216); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2216]; `tensor/DDL_lfc|DDL_z.npy` [2216]; `embed/gene_vectors.npy` [2216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2216 or target_col == 2216). Every well: [[PCSK1N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK1N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
