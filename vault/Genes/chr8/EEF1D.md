---
symbol: "EEF1D"
type: "gene"
col: 2472
ensembl_id: "ENSG00000104529"
name: "eukaryotic translation elongation factor 1 delta"
location: "8q24.3"
module: 43
arm: "+"
pooled_cpm: 169.23
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EEF1D

*eukaryotic translation elongation factor 1 delta* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +7.8, q 3e-12, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +4.4, q 0.002, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 4.28×, NCI-H1573 4.71×, SW 900 3.43×, LoVo 3.54×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 4.26×, A-427 2.97×, C-33 A 3.01×, NCI-H1792 3.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 3.95×, C32 2.89×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.133×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.368×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS3]] (+0.77, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPS12]] (+0.76, fdr 7e-06), [[RPL37A]] (+0.75, fdr 7e-06, ⚠ RPL37A in the vector space only through flagged drug-doses), [[RPS19]] (+0.74, fdr 1e-05), [[SNHG6]] (+0.74, fdr 7e-06); moves opposite to [[PNPO]] (-0.63, fdr 3e-05), [[RBBP9]] (-0.61, fdr 2e-05), [[ALG10]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 4.28×, NCI-H1573 4.71×, SW 900 3.43×, LoVo 3.54×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 4.26×, A-427 2.97×, C-33 A 3.01×, NCI-H1792 3.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 3.95×, C32 2.89×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.77×** | +7.8 | 3e-12 | 47/49 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.18×** | +6.9 | 2e-09 | 42/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.91×** | +4.6 | 9e-04 | 41/45 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.002 | 37/49 (NCI-H2347, A549, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.53×** | +3.9 | 0.010 | 35/48 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +3.9 | 0.010 | 38/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.51×** | +3.8 | 0.013 | 36/48 (KATO III, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.6 | 0.020 | 41/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.45×** | +3.4 | 0.040 | 36/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.44×** | +3.2 | 0.075 | 33/47 (COLO 205, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.41× | +3.0 | 0.13 | 28/50 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.133×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.368×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.750× | -3.7 | 0.13 | 37/48 (C32, KATO III, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 179 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +8.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 96.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 198 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 159 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.133× (z -9.1) |
| [[SW 900 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 197 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 247 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 260 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 322 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 136 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS3]] ⚠ | +0.77 | +0.63 / +0.81 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 931; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.76 | +0.60 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 803 |
| [[RPL37A]] ⚠ | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 677; ⚠ in the vector space only through flagged drug-doses |
| [[RPS19]] | +0.74 | +0.57 / +0.79 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 952 |
| [[SNHG6]] | +0.74 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[RPL9]] ⚠ | +0.74 | +0.54 / +0.78 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 770; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 672 |
| [[RPS17]] ⚠ | +0.73 | +0.57 / +0.77 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 864; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.73 | +0.52 / +0.78 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 741 |
| [[UBA52]] | +0.73 | +0.52 / +0.80 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 890 |
| [[RPLP1]] | +0.73 | +0.52 / +0.79 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 918 |
| [[RPL31]] | +0.72 | +0.52 / +0.78 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 898 |
| [[RPL26]] | +0.71 | +0.49 / +0.79 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 806 |
| [[RPS27]] | +0.71 | +0.53 / +0.77 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 716 |
| [[RPL12]] | +0.71 | +0.46 / +0.79 | both halves | 3e-05 | pathway: Eukaryotic Translation Elongation; STRING 816 |
| [[RPS8]] | +0.70 | +0.46 / +0.78 | both halves | 3e-05 | pathway: Eukaryotic Translation Elongation; STRING 900 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.63 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[RBBP9]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[ALG10]] | -0.60 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[ALG10B]] | -0.58 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[SMIM15]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.57 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[DR1]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CEP41]] | -0.56 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[COX11]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[COPS6]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[DLAT]] | -0.55 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SRP9]] | -0.55 | -0.45 / -0.65 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.5, -27.1); signed map (-59.0, -4.0). **Vector** length 74.9, 32.7% of its response variance represented; |z| ≥ 3 in 562 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Peptide chain elongation* (reactome, mean cos +0.63 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.62 to 53); *Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC)* (reactome, mean cos +0.63 to 52).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.0 | +3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +1.6 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -6.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.2 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,579,697-143,599,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EF-1D, FLJ20897 |
| Reactome | 2 pathways, smallest: Eukaryotic Translation Elongation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P29692](https://www.uniprot.org/uniprotkb/P29692) (Elongation factor 1-delta):

> [Isoform 1]: EF-1-beta and EF-1-delta stimulate the exchange of GDP bound to EF-1-alpha to GTP, regenerating EF-1-alpha for another round of transfer of aminoacyl-tRNAs to the ribosome.; [Isoform 2]: Regulates induction of heat-shock-responsive genes through association with heat shock transcription factors and direct DNA-binding at heat shock promoter elements (HSE).

**Summary**, from NCBI Gene [1936](https://www.ncbi.nlm.nih.gov/gene/1936):

> This gene encodes a subunit of the elongation factor-1 complex, which is responsible for the enzymatic delivery of aminoacyl tRNAs to the ribosome. This subunit, delta, functions as guanine nucleotide exchange factor. It is reported that following HIV-1 infection, this subunit interacts with HIV-1 Tat. This interaction results in repression of translation of host cell proteins and enhanced translation of viral proteins. Several alternatively spliced transcript variants encoding multiple …

**Accessions** — [HGNC:3211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3211) · Entrez [1936](https://www.ncbi.nlm.nih.gov/gene/1936) · UniProt [P29692](https://www.uniprot.org/uniprotkb/P29692) · Ensembl [ENSG00000104529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104529)

## Data

Gene col 2472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2472); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2472]; `tensor/DDL_lfc|DDL_z.npy` [2472]; `embed/gene_vectors.npy` [2472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2472 or target_col == 2472). Every well: [[EEF1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
