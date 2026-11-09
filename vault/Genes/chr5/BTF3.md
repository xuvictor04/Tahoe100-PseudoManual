---
symbol: "BTF3"
type: "gene"
col: 7022
ensembl_id: "ENSG00000145741"
name: "basic transcription factor 3"
location: "5q13.2"
module: 43
arm: "+"
pooled_cpm: 157.06
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# BTF3

*basic transcription factor 3* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.20× (z +9.5, q 1e-18, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.45× (z +3.4, q 0.036, up in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (COLO 205 5.95×, SW480 4.36×, C-33 A 4.61×, LoVo 3.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 4.34×, KATO III 3.69×, A498 3.94×, NCI-H460 3.96×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.19×; ⚠ cell-cycle shift, explains ~0% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL30]] (+0.86, fdr 7e-06, ⚠ RPL30 in the vector space only through flagged drug-doses), [[NACA]] (+0.83, fdr 7e-06, ⚠ NACA in the vector space only through flagged drug-doses), [[RPS4X]] (+0.80, fdr 7e-06), [[RPL7]] (+0.77, fdr 7e-06), [[RPL19]] (+0.76, fdr 7e-06); moves opposite to [[DNMT1]] (-0.55, fdr 2e-05), [[PKMYT1]] (-0.55, fdr 3e-05), [[XRCC3]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (COLO 205 5.95×, SW480 4.36×, C-33 A 4.61×, LoVo 3.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 4.34×, KATO III 3.69×, A498 3.94×, NCI-H460 3.96×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.19×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +9.5 | 1e-18 | 48/49 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.4 | 1e-18 | 44/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +6.9 | 1e-09 | 42/45 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.73×** | +5.1 | 6e-05 | 44/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.74×** | +4.9 | 1e-04 | 44/47 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.66×** | +4.7 | 3e-04 | 45/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.3 | 0.001 | 42/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.55×** | +4.1 | 0.004 | 37/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.036 | 35/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.039 | 30/48 (AN3 CA, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.39× | +3.0 | 0.12 | 29/48 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 178 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +10.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 288 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 193 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 172 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 95.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 97.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 291 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 195 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 87.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 190 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL30]] ⚠ | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | STRING 993; ⚠ in the vector space only through flagged drug-doses |
| [[NACA]] ⚠ | +0.83 | +0.79 / +0.83 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS4X]] | +0.80 | +0.73 / +0.84 | both halves | 7e-06 | STRING 731 |
| [[RPL7]] | +0.77 | +0.70 / +0.86 | both halves | 7e-06 | STRING 964 |
| [[RPL19]] | +0.76 | +0.72 / +0.82 | both halves | 7e-06 | STRING 979 |
| [[RPL37]] ⚠ | +0.75 | +0.68 / +0.79 | both halves | 7e-06 | STRING 896; ⚠ in the vector space only through flagged drug-doses |
| [[RPL5]] | +0.73 | +0.72 / +0.78 | both halves | 7e-06 | STRING 954 |
| [[RPL24]] | +0.72 | +0.73 / +0.75 | both halves | 7e-06 | STRING 984 |
| [[RPL21]] ⚠ | +0.72 | +0.66 / +0.72 | both halves | 7e-06 | STRING 974; ⚠ in the vector space only through flagged drug-doses |
| [[RPS20]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 | STRING 668 |
| [[RPL10A]] ⚠ | +0.70 | +0.71 / +0.73 | both halves | 7e-06 | STRING 979; ⚠ in the vector space only through flagged drug-doses |
| [[RPL11]] | +0.70 | +0.65 / +0.80 | both halves | 7e-06 | STRING 981 |
| [[NSA2]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[EEF1G]] | +0.69 | +0.58 / +0.78 | both halves | 7e-06 | STRING 772 |
| [[EEF1B2]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | STRING 637 |
| [[RPL14]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | STRING 965 |
| [[RPS8]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 | STRING 900 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PKMYT1]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[XRCC3]] | -0.54 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[RECQL4]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MCM10]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SAE1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TEDC1]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[THOP1]] | -0.52 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[E2F1]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CLSPN]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.0, -29.4); signed map (-59.9, -6.1). **Vector** length 54.7, 22.5% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.64 to 55); *Peptide chain elongation* (reactome, mean cos +0.64 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.64 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +3.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.0 | +0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | +0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | +0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -0.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | -1.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | basic transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,498,408-73,505,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTF3a, BTF3b; previously NACB |
| Reactome | 3 pathways, smallest: Dengue Virus Genome Translation and Replication; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P20290](https://www.uniprot.org/uniprotkb/P20290) (Transcription factor BTF3):

> When associated with NACA, prevents inappropriate targeting of non-secretory polypeptides to the endoplasmic reticulum (ER). Binds to nascent polypeptide chains as they emerge from the ribosome and blocks their interaction with the signal recognition particle (SRP), which normally targets nascent secretory peptides to the ER. BTF3 is also a general transcription factor that can form a stable complex with RNA polymerase II. Required for the initiation of transcription.

**Summary**, from NCBI Gene [689](https://www.ncbi.nlm.nih.gov/gene/689):

> This gene encodes the basic transcription factor 3. This protein forms a stable complex with RNA polymerase IIB and is required for transcriptional initiation. Alternative splicing results in multiple transcript variants encoding different isoforms. This gene has multiple pseudogenes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1125) · Entrez [689](https://www.ncbi.nlm.nih.gov/gene/689) · UniProt [P20290](https://www.uniprot.org/uniprotkb/P20290) · Ensembl [ENSG00000145741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145741)

## Data

Gene col 7022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7022); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7022]; `tensor/DDL_lfc|DDL_z.npy` [7022]; `embed/gene_vectors.npy` [7022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7022 or target_col == 7022). Every well: [[BTF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
