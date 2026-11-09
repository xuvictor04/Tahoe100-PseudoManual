---
symbol: "DDX19A-DT"
type: "gene"
col: 15366
ensembl_id: "ENSG00000261777"
name: "DDX19A divergent transcript"
location: "16q22.1"
module: 35
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DDX19A-DT

*DDX19A divergent transcript* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +18.5, q 0e+00, up in 37 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0743×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0774×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.83, fdr 7e-06), [[PAXBP1-AS1]] (+0.83, fdr 7e-06), [[SUMO2P17]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02175]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +18.5 | 0e+00 | 37/38 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +12.1 | 5e-31 | 25/37 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +11.6 | 1e-28 | 7/10 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +10.6 | 4e-24 | 14/21 (NCI-H2030, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.8 | 1e-20 | 2/6 (PANC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +8.6 | 8e-16 | 19/45 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.0 | 2e-07 | 12/34 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.9 | 2e-07 | 13/43 (SW480, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 10/46 (A498, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.004 | 6/42 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.023 | 3/26 (NCI-H2030, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.1 | 0.085 | 3/9 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15366.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0743×); [[Tofacitinib (citrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0774×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.754× | -3.4 | 0.21 | 11/44 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.4 | 0.21 | 12/48 (SW48, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.22 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +10.9) | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0743× (z -11.5) |
| [[A498 (line)]] | wt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +9.3) | — |
| [[LoVo (line)]] | wt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 5.75 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0774× (z -9.4) |
| [[SW480 (line)]] | alt | 5.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.9) | — |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.83 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.83 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[SUMO2P17]] | +0.83 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.80 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.77 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.77 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.77 | +0.81 / +0.50 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.77 | +0.75 / +0.58 | both halves | 7e-06 | same gene group |
| [[MALINC1]] | +0.76 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[PGBD4]] | +0.76 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.76 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02175]] | B | LINC02175 activity raises DDX19A-DT's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.10× lower at baseline in the lines without LINC02175 | 0.035 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.875). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.1, 21.6); signed map (30.0, -2.3). **Vector** length 46.3, 5.02% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +18.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DDX19A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q22.1 — chr16:70,315,442-70,346,806 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55349) · Entrez [100506083](https://www.ncbi.nlm.nih.gov/gene/100506083) · Ensembl [ENSG00000261777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261777)

## Data

Gene col 15366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15366); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15366]; `tensor/DDL_lfc|DDL_z.npy` [15366]; `embed/gene_vectors.npy` [15366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15366 or target_col == 15366). Every well: [[DDX19A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX19A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
