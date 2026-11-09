---
symbol: "RPS2"
type: "gene"
col: 6473
ensembl_id: "ENSG00000140988"
name: "ribosomal protein S2"
location: "16p13.3"
module: 43
arm: "+"
pooled_cpm: 220.29
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS2

*ribosomal protein S2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.27× (z +8.9, q 3e-16, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +5.3, q 2e-05, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.49×, C32 5.10×, Hs 766T 4.37×, A-172 4.46×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 5.24×, C32 5.81×, Hs 766T 4.86×, NCI-H1573 5.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 3.00×, NCI-H2347 2.78×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.831× (z -4.8, q 8e-04, down in 28 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.583× (z -4.2, q 0.007, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.268×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0]] (+0.82, fdr 7e-06), [[RPS20]] (+0.82, fdr 7e-06), [[RPS4X]] (+0.82, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.63, fdr 3e-05), [[MIS12]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLR4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EEF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6473.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.49×, C32 5.10×, Hs 766T 4.37×, A-172 4.46×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 5.24×, C32 5.81×, Hs 766T 4.86×, NCI-H1573 5.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 3.00×, NCI-H2347 2.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.27×** | +8.9 | 3e-16 | 44/44 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.67×** | +8.8 | 3e-16 | 49/49 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.49×** | +6.6 | 7e-09 | 44/45 (KATO III, C32, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.3 | 2e-05 | 36/49 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.64×** | +3.7 | 0.018 | 38/47 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.7 | 0.018 | 32/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.56×** | +3.5 | 0.041 | 39/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.56×** | +3.4 | 0.054 | 37/50 (A-172, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6473.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.268×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.831×** | -4.8 | 8e-04 | 28/50 (J82, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -4.2 | 0.007 | 34/48 (SNU-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 140 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.0) | — |
| [[KATO III (line)]] | alt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 240 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 201 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 305 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 244 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 221 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 277 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 255 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 365 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 159 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 199 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 297 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.9) |
| [[A-427 (line)]] | wt | 296 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 265 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 359 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 257 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 334 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 337 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 353 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0]] | +0.82 | +0.76 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPS20]] | +0.82 | +0.77 / +0.81 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS4X]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL12]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RACK1]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL7]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13A]] | +0.80 | +0.70 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.79 | +0.73 / +0.75 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.79 | +0.73 / +0.77 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS7]] | +0.79 | +0.77 / +0.69 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPLP1]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL39]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.63 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[MIS12]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR4]] | B | TLR4 activity lowers RPS2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without TLR4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF2]] | C | RPS2's natural level weakens EEF2's drug response | RPS2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.20; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.9, -29.9); signed map (-60.9, -6.5). **Vector** length 78.3, 30.7% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.71 to 34); *oxidative phosphorylation* (hallmark, mean cos +0.52 to 9); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.63 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.0 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.5 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.8 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,962,058-1,964,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LLREP3, S2, uS5 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 58 pathways, smallest: Protein methylation; RMTs methylate histone arginines; SARS-CoV-1 modulates host translation machinery |
| Matched by | ensembl_id |

**Function**, from UniProt [P15880](https://www.uniprot.org/uniprotkb/P15880) (Small ribosomal subunit protein uS5):

> Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a …

**Summary**, from NCBI Gene [6187](https://www.ncbi.nlm.nih.gov/gene/6187):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S5P family of ribosomal proteins. It is located in the cytoplasm. This gene shares sequence similarity with mouse LLRep3. It is co-transcribed with the small nucleolar RNA …

**Accessions** — [HGNC:10404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10404) · Entrez [6187](https://www.ncbi.nlm.nih.gov/gene/6187) · UniProt [P15880](https://www.uniprot.org/uniprotkb/P15880) · Ensembl [ENSG00000140988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140988)

## Data

Gene col 6473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6473); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6473]; `tensor/DDL_lfc|DDL_z.npy` [6473]; `embed/gene_vectors.npy` [6473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6473 or target_col == 6473). Every well: [[RPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
