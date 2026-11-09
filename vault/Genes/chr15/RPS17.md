---
symbol: "RPS17"
type: "gene"
col: 11325
ensembl_id: "ENSG00000182774"
name: "ribosomal protein S17"
location: "15q25.2"
module: 43
arm: "+"
pooled_cpm: 266.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS17

*ribosomal protein S17* — 15q25.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.71× (z +7.7, q 6e-12, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (LoVo 4.73×, MIA PaCa-2 5.42×, Hs 766T 4.72×, SK-MEL-2 4.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.294×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL31]] (+0.97, fdr 7e-06), [[RPL35A]] (+0.97, fdr 7e-06), [[RPL26]] (+0.97, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (LoVo 4.73×, MIA PaCa-2 5.42×, Hs 766T 4.72×, SK-MEL-2 4.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.71×** | +7.7 | 6e-12 | 49/49 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.99×** | +6.0 | 5e-07 | 44/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.3 | 0.003 | 47/47 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.30×** | +4.2 | 0.004 | 41/45 (Hs 766T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.02×** | +4.2 | 0.004 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.84×** | +3.6 | 0.030 | 43/48 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | 1.73× | +3.0 | 0.19 | 38/47 (A-172, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.294×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.659× | -3.5 | 0.31 | 35/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 377 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 282 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.3) |
| [[Hs 766T (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 567 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 242 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 191 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 285 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 247 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 268 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 296 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 164 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 283 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 397 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 280 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 272 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 354 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 252 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 434 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL31]] | +0.97 | +0.92 / +0.98 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.97 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL9]] ⚠ | +0.97 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35]] ⚠ | +0.96 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.96 | +0.90 / +0.98 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | +0.95 | +0.90 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL17]] | +0.95 | +0.88 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL27]] | +0.94 | +0.88 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.962). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.3, -27.4); signed map (-59.9, -4.2). **Vector** length 80.3, 54.1% of its response variance represented; |z| ≥ 3 in 416 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.87 to 34); *MYC targets v1* (hallmark, mean cos +0.65 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.70 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.9 | -0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.6 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | +0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | -0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,536,750-82,540,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPS17L1, RPS17L2, MGC72007, S17, eS17; previously RPS17L |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P08708](https://www.uniprot.org/uniprotkb/P08708) (Small ribosomal subunit protein eS17):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6218](https://www.ncbi.nlm.nih.gov/gene/6218):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of four RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S17E family of ribosomal proteins and is located in the cytoplasm. Mutations in this gene cause Diamond-Blackfan anemia 4. Alternative splicing of this gene results in …

**Accessions** — [HGNC:10397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10397) · Entrez [6218](https://www.ncbi.nlm.nih.gov/gene/6218) · UniProt [P08708](https://www.uniprot.org/uniprotkb/P08708) · Ensembl [ENSG00000182774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182774)

## Data

Gene col 11325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11325); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11325]; `tensor/DDL_lfc|DDL_z.npy` [11325]; `embed/gene_vectors.npy` [11325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11325 or target_col == 11325). Every well: [[RPS17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
