---
symbol: "RPL38"
type: "gene"
col: 10299
ensembl_id: "ENSG00000172809"
name: "ribosomal protein L38"
location: "17q25.1"
module: 131
arm: "+"
pooled_cpm: 175.47
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL38

*ribosomal protein L38* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.00× (z +9.5, q 8e-19, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (NCI-H460 5.48×, Panc 03.27 5.01×, LoVo 5.24×, NCI-H1573 5.71×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.310×, C-33 A 0.345×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS10]] (+0.94, fdr 7e-06), [[RPS21]] (+0.94, fdr 7e-06), [[RPS11]] (+0.93, fdr 7e-06); moves opposite to [[PNPO]] (-0.66, fdr 7e-06), [[DCLRE1A]] (-0.64, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10299.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 14 lines (NCI-H460 5.48×, Panc 03.27 5.01×, LoVo 5.24×, NCI-H1573 5.71×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.00×** | +9.5 | 8e-19 | 48/49 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.06×** | +7.6 | 1e-11 | 44/44 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.62×** | +5.3 | 2e-05 | 42/45 (SNU-423, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.07×** | +5.1 | 4e-05 | 45/48 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **2.02×** | +4.9 | 9e-05 | 48/48 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.3 | 0.001 | 45/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.37× | +3.1 | 0.15 | 27/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 1.57× | +3.1 | 0.15 | 33/47 (A-172, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.54× | +3.0 | 0.16 | 36/48 (A-172, COLO 205, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10299.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.310×, C-33 A 0.345×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.720× | -3.3 | 0.63 | 28/48 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 198 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 229 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 218 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.6) |
| [[COLO 205 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 244 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 230 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 238 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 242 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 209 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 197 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 338 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 202 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 211 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 201 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS10]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS11]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.92 | +0.84 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.90 | +0.80 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15]] ⚠ | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS24]] | +0.88 | +0.75 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL24]] | +0.87 | +0.75 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.66 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.947). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.1, -27.1); signed map (-61.7, -3.1). **Vector** length 77.7, 43.5% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.89 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.90 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.90 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.4 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.6 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,203,582-74,210,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L38, eL38 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P63173](https://www.uniprot.org/uniprotkb/P63173) (Large ribosomal subunit protein eL38):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6169](https://www.ncbi.nlm.nih.gov/gene/6169):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L38E family of ribosomal proteins. It is located in the cytoplasm. Alternative splice variants have been identified, both encoding the same protein. As is typical for genes …

**Accessions** — [HGNC:10349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10349) · Entrez [6169](https://www.ncbi.nlm.nih.gov/gene/6169) · UniProt [P63173](https://www.uniprot.org/uniprotkb/P63173) · Ensembl [ENSG00000172809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172809)

## Data

Gene col 10299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10299); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10299]; `tensor/DDL_lfc|DDL_z.npy` [10299]; `embed/gene_vectors.npy` [10299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10299 or target_col == 10299). Every well: [[RPL38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
