---
symbol: "SMC1A"
type: "gene"
col: 1020
ensembl_id: "ENSG00000072501"
name: "structural maintenance of chromosomes 1A"
location: "Xp11.22"
module: 6
arm: "+"
pooled_cpm: 153.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# SMC1A

*structural maintenance of chromosomes 1A* — Xp11.22

> [!summary] In one line
> SMC1A is an ATPase subunit of the cohesin ring that holds sister chromatids together, and is also a direct ATM substrate in the DNA-damage response.

## What it is

SMC1A heterodimerises with SMC3 through long coiled-coil arms joined at a hinge; RAD21 and a STAG subunit close the ring entrapping sister chromatids from replication until anaphase, and the same complex organises chromatin loops with CTCF. Beyond cohesion, SMC1A is phosphorylated by [[ATM]] on two C-terminal serines after ionising radiation, a step required for the S-phase checkpoint: cohesin is part of the damage response, not only the scaffold. The gene is X-linked: missense variants give a Cornelia de Lange phenotype, truncating variants a distinct epileptic encephalopathy. Cohesin subunits are recurrently mutated in myeloid malignancy and bladder cancer.

## What is uncertain

SMC1A is not a canonical direct p53 target. No p53 repressive element at this gene is established, and indirect repression through [[The p21-DREAM axis]] explains cohesin and mitotic genes at least as well, the route that also moves [[SGO1]] and [[KIF11]]. Being essential and well expressed in every line, its dynamic range is narrow: a small coordinated fall is what cell-cycle exit alone produces. The direct-versus-indirect question is open.

## References

- Kim et al., 2002, Genes & Development — ATM-dependent and ATM-independent phosphorylation of SMC1 in response to DNA damage.
- Musio et al., 2006, Nature Genetics — SMC1A mutations cause X-linked Cornelia de Lange syndrome.
- Nasmyth & Haering, 2009, Annual Review of Genetics — review of cohesin ring architecture and its roles.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.03× (z +19.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.33× (z +3.9, q 0.004, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.729× (z -6.4, q 8e-08, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~81% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 6 lines (A-427 0.434×, A498 0.491×, C32 0.441×, A-172 0.469×, …; ⚠ cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.457×, SNU-1 0.300×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (BT-474 0.449×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNMT1]] (+0.82, fdr 7e-06), [[XRCC2]] (+0.79, fdr 7e-06), [[MCM8]] (+0.78, fdr 7e-06); moves opposite to [[POLR1D]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **4.03×** | +19.9 | 0e+00 | 49/49 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.89×** | +18.7 | 0e+00 | 44/44 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.71×** | +13.1 | 4e-37 | 43/45 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.55×** | +6.3 | 5e-08 | 39/48 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.55×** | +6.2 | 5e-08 | 37/48 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.43×** | +5.1 | 3e-05 | 36/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **1.43×** | +4.9 | 7e-05 | 30/47 (SNU-423, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.41×** | +4.7 | 1e-04 | 32/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.26×** | +4.6 | 3e-04 | 34/48 (HT-29, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.38×** | +4.5 | 3e-04 | 32/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +4.3 | 8e-04 | 32/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.34×** | +4.0 | 0.003 | 31/50 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.004 | 30/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.010 | 30/47 (A549, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 1.20× | +3.6 | 0.010 | 22/48 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.015 | 25/47 (H4, HOP62, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.016 | 31/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 6 lines (A-427 0.434×, A498 0.491×, C32 0.441×, A-172 0.469×, …; ⚠ cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.457×, SNU-1 0.300×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (BT-474 0.449×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.729×** | -6.4 | 8e-08 | 37/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.697×** | -5.2 | 7e-05 | 36/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.778×** | -3.6 | 0.054 | 28/49 (Hs 766T, HOP62, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.685×** | -3.6 | 0.054 | 29/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.843× | -3.5 | 0.058 | 19/48 (HCT15, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.845× | -3.4 | 0.058 | 19/48 (KATO III, HCT15, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.722× | -3.0 | 0.19 | 25/48 (Hs 766T, H4, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 125 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LoVo (line)]] | wt | 116 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 149 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 61.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2347 (line)]] | alt | 87.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 122 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.469× (z -9.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-427 (line)]] | wt | 207 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.50× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.434× (z -13.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A498 (line)]] | wt | 137 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.491× (z -10.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[C32 (line)]] | wt | 110 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.441× (z -10.4) ⚠ cell-cycle shift, explains ~81% of this change |
| [[CFPAC-1 (line)]] | alt | 70.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 114 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.422× (z -9.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[MIA PaCa-2 (line)]] | alt | 83.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[H4 (line)]] | wt | 120 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.429× (z -8.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HOP62 (line)]] | alt | 153 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HS-578T (line)]] | alt | 87.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 194 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 65.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[KATO III (line)]] | alt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 67.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1573 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 79.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 177 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RPMI-7951 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-1 (line)]] | wt | 92.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 78.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW1417 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 273 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 53.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[BT-474 (line)]] | alt | 155 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Belinostat (drug)]] 0.5 µM 0.449× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 84.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.12× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HCT15 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HEC-1-A (line)]] | alt | 283 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HepG2_C3A (line)]] | wt | 95.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW48 (line)]] | wt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[J82 (line)]] | alt | 262 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SHP-77 (line)]] | alt | 484 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AN3 CA (line)]] | alt | 262 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 290 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT1]] | +0.82 | +0.76 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 496 |
| [[XRCC2]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[MCM8]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 | pathway: S Phase |
| [[CLSPN]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[ATAD2]] | +0.77 | +0.73 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS |
| [[MCM10]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[HELLS]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[VRK1]] | +0.74 | +0.74 / +0.76 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[BRIP1]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[E2F8]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[POLE]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 469 |
| [[MCM3]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 614 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1D]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises SMC1A's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without CDC25A | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises SMC1A's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without E2F8 | 0.094 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.2, -42.7); signed map (-36.5, -48.0). **Vector** length 129, 51.6% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.60 to 28); *DNA Replication* (reactome, mean cos +0.59 to 40); *E2F G1/S* (control, mean cos +0.59 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +5.7 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +5.6 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.3 | +6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.1 | +2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.8 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -9.2 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -5.9 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,374,149-53,422,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS423E, KIAA0178, SB1.8, Smcb; previously SMC1L1 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; Cohesin complex; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 21 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14683](https://www.uniprot.org/uniprotkb/Q14683) (Structural maintenance of chromosomes protein 1A):

> Involved in chromosome cohesion during cell cycle and in DNA repair. Central component of cohesin complex. The cohesin complex is required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. The cohesin complex may also play a role in spindle pole assembly during …

**Summary**, from NCBI Gene [8243](https://www.ncbi.nlm.nih.gov/gene/8243):

> Proper cohesion of sister chromatids is a prerequisite for the correct segregation of chromosomes during cell division. The cohesin multiprotein complex is required for sister chromatid cohesion. This complex is composed partly of two structural maintenance of chromosomes (SMC) proteins, SMC3 and either SMC1B or the protein encoded by this gene. Most of the cohesin complexes dissociate from the chromosomes before mitosis, although those complexes at the kinetochore remain. Therefore, the …

**Accessions** — [HGNC:11111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11111) · Entrez [8243](https://www.ncbi.nlm.nih.gov/gene/8243) · UniProt [Q14683](https://www.uniprot.org/uniprotkb/Q14683) · Ensembl [ENSG00000072501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072501)

## Data

Gene col 1020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1020); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1020]; `tensor/DDL_lfc|DDL_z.npy` [1020]; `embed/gene_vectors.npy` [1020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1020 or target_col == 1020). Every well: [[SMC1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SMC1A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
