---
symbol: "NEMP2-DT"
type: "gene"
col: 13917
ensembl_id: "ENSG00000233654"
name: "NEMP2 divergent transcript"
location: "2q32.2"
module: 10
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# NEMP2-DT

*NEMP2 divergent transcript* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.53× (z +11.5, q 8e-28, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +11.4, q 1e-27, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.626× (z -4.4, q 0.005, down in 15 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.0236×, LoVo 0.120×; ⚠ cell-cycle shift, explains ~44% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (LS 180 0.0691×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.171×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.196×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26-AS1]] (+0.75, fdr 1e-05), [[GUCY2C-AS1]] (+0.68, fdr 3e-05), [[ANGPT2]] (+0.68, fdr 5e-05); moves opposite to [[GGCX]] (-0.57, fdr 5e-05), [[YIPF1]] (-0.57, fdr 9e-04, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HYDIN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.5 | 8e-28 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +11.4 | 1e-27 | 24/32 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.7 | 2e-24 | 11/17 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +9.1 | 1e-17 | 17/34 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +6.6 | 4e-09 | 3/6 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +6.5 | 7e-09 | 16/31 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.3 | 8e-06 | 6/14 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 8/44 (AsPC-1, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.4 | 6e-04 | 2/14 (PANC-1, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.4 | 6e-04 | 12/42 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 7e-04 | 6/26 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.3 | 9e-04 | 9/42 (C-33 A, A498, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 9/45 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.001 | 14/42 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.001 | 4/20 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.025 | 6/36 (A-172, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.042 | 5/35 (J82, C-33 A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.062 | 7/38 (HCT15, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.067 | 7/25 (LoVo, J82, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.0236×, LoVo 0.120×; ⚠ cell-cycle shift, explains ~44% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (LS 180 0.0691×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.171×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -4.4 | 0.005 | 15/39 (LS 180, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -3.7 | 0.061 | 13/42 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.30 | 13/42 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.725× | -3.1 | 0.30 | 13/42 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 8.50 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -10.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 9.63 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -10.0) |
| [[LS 180 (line)]] | wt | 6.88 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0691× (z -10.5) |
| [[RKO (line)]] | wt | 6.66 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0236× (z -11.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.979 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26-AS1]] | +0.75 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | +0.68 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[ANGPT2]] | +0.68 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[LEKR1]] | +0.68 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[NANOS3]] | +0.67 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PRSS48]] | +0.66 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NEB]] | +0.65 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[FBXO38-DT]] | +0.65 | +0.68 / +0.34 | both halves | 1e-04 | same gene group |
| [[CACNA1E]] | +0.65 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[PGBD4]] | +0.64 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.64 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[LINC00486]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCX]] | -0.57 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[YIPF1]] | -0.57 | -0.63 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYDIN]] | B | HYDIN activity lowers NEMP2-DT's level | lines that do not express HYDIN (9) vs lines expressing it (41) | 2.11× higher at baseline in the lines without HYDIN | 0.048 | ⚠ within organs, on part of the lines; also absent: SNRPN, ZNF613, MOCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (10.2, 16.0); signed map (26.4, 3.4). **Vector** length 52.6, 6.92% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | NEMP2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q32.2 — chr2:190,534,855-190,569,776 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55713) · Entrez [105376748](https://www.ncbi.nlm.nih.gov/gene/105376748) · Ensembl [ENSG00000233654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233654)

## Data

Gene col 13917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13917); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13917]; `tensor/DDL_lfc|DDL_z.npy` [13917]; `embed/gene_vectors.npy` [13917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13917 or target_col == 13917). Every well: [[NEMP2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEMP2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
