---
symbol: "FRG1"
type: "gene"
col: 3060
ensembl_id: "ENSG00000109536"
name: "FSHD region gene 1"
location: "4q35.2"
module: 12
arm: "+"
pooled_cpm: 19.31
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FRG1

*FSHD region gene 1* — 4q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +12.7, q 5e-34, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.71× (z +9.4, q 1e-18, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.509× (z -6.4, q 9e-08, down in 39 of 48 measured lines) ⚠ unreliable plate only.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.79, fdr 7e-06), [[TRIM23]] (+0.76, fdr 7e-06), [[PPIG]] (+0.75, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.68, fdr 7e-06), [[TXNDC5]] (-0.65, fdr 7e-06), [[PPT1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENKD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.57×** | +12.7 | 5e-34 | 45/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +9.4 | 1e-18 | 44/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.64×** | +8.9 | 1e-16 | 44/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +6.1 | 1e-07 | 37/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.90×** | +6.1 | 1e-07 | 40/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.18×** | +5.7 | 9e-07 | 36/48 (SW 900, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +5.6 | 2e-06 | 34/47 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.5 | 3e-06 | 31/48 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.2 | 1e-05 | 33/44 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.72×** | +5.2 | 1e-05 | 37/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +5.0 | 3e-05 | 35/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.65×** | +4.7 | 1e-04 | 30/45 (C32, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.60×** | +4.3 | 7e-04 | 27/46 (NCI-H460, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 7e-04 | 29/47 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 25/47 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.014 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.024 | 24/47 (KATO III, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.031 | 21/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +3.2 | 0.047 | 21/44 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.509×** | -6.4 | 9e-08 | 39/48 (AsPC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.2 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +16.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.63× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 30.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +17.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.6× (z +11.8) | — |
| [[A549 (line)]] | wt | 16.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +20.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.26× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.06× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +18.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 18.2× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 12.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +10.3) | — |
| [[A498 (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.37× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +14.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +11.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +11.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.79 | +0.67 / +0.80 | both halves | 7e-06 | STRING 901 |
| [[TRIM23]] | +0.76 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[PPIG]] | +0.75 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | +0.75 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[RP9]] | +0.73 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[SYF2]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 | STRING 829 |
| [[C18orf21]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[EAPP]] | +0.70 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[IK]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.68 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.65 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[PPT1]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[AHCY]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[MDH2]] | -0.64 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.62 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[EMC1]] | -0.62 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[LAPTM4B]] | -0.62 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.61 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[PAICS]] | -0.60 | -0.50 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENKD1]] | B | ENKD1 activity lowers FRG1's level | lines that do not express ENKD1 (5) vs lines expressing it (45) | 1.24× higher at baseline in the lines without ENKD1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.0, -28.7); signed map (-14.5, -5.8). **Vector** length 75.1, 19.1% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.53 to 17); *mRNA Splicing* (reactome, mean cos +0.53 to 17); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.50 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.2 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +9.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.1 | +8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.2 — chr4:189,940,855-189,963,202 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FSG1, FRG1A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14331](https://www.uniprot.org/uniprotkb/Q14331) (Protein FRG1):

> Binds to mRNA in a sequence-independent manner. May play a role in regulation of pre-mRNA splicing or in the assembly of rRNA into ribosomal subunits. May be involved in mRNA transport. May be involved in epigenetic regulation of muscle differentiation through regulation of activity of the histone-lysine N-methyltransferase KMT5B.

**Summary**, from NCBI Gene [2483](https://www.ncbi.nlm.nih.gov/gene/2483):

> This gene maps to a location 100 kb centromeric of the repeat units on chromosome 4q35 which are deleted in facioscapulohumeral muscular dystrophy (FSHD). It is evolutionarily conserved and has related sequences on multiple human chromosomes but DNA sequence analysis did not reveal any homology to known genes. In vivo studies demonstrate the encoded protein is localized to the nucleolus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3954) · Entrez [2483](https://www.ncbi.nlm.nih.gov/gene/2483) · UniProt [Q14331](https://www.uniprot.org/uniprotkb/Q14331) · Ensembl [ENSG00000109536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109536)

## Data

Gene col 3060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3060); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3060]; `tensor/DDL_lfc|DDL_z.npy` [3060]; `embed/gene_vectors.npy` [3060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3060 or target_col == 3060). Every well: [[FRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
